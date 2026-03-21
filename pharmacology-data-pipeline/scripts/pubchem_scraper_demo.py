"""
Pharmacology Data Pipeline (Demo Version)

This script demonstrates how pharmacological properties of compounds
can be extracted from PubChem and classified into structured categories.

Note:
This is a simplified demonstration version. It uses sample input files
and may require adjustments to run in a real environment.
"""

import pandas as pd
import unicodedata
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ------------------------
# Utility functions
# ------------------------

def normalize_text(text):
    return unicodedata.normalize('NFKC', str(text)).strip().lower()

# ------------------------
# Load sample input
# ------------------------

df = pd.read_excel("inputs/sample_substances.xlsx")

# Example simplified property list
PROPERTIES = [
    "stimulant", "sedative", "analgesic",
    "anti-inflammatory", "hallucinogenic"
]

for prop in PROPERTIES:
    df[prop] = "FALSE"

# ------------------------
# Setup Selenium (headless)
# ------------------------

def init_driver():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)

# ------------------------
# Scraping logic (simplified)
# ------------------------

def scrape_pubchem(compound_name):
    driver = init_driver()
    try:
        driver.get("https://pubchem.ncbi.nlm.nih.gov/")
        search_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        search_box.send_keys(compound_name)
        search_box.submit()

        page_source = driver.page_source.lower()

        result = {}
        for prop in PROPERTIES:
            result[prop] = "TRUE" if prop in page_source else "FALSE"

        return result

    except Exception as e:
        return {prop: "ERROR" for prop in PROPERTIES}

    finally:
        driver.quit()

# ------------------------
# Apply scraping
# ------------------------

for idx, row in df.iterrows():
    compound = row["Compound_Name"]
    properties = scrape_pubchem(compound)

    for prop, value in properties.items():
        df.loc[idx, prop] = value

# ------------------------
# Simple classification
# ------------------------

def classify_row(row):
    if row["stimulant"] == "TRUE":
        return "Stimulant"
    elif row["sedative"] == "TRUE":
        return "Depressant"
    elif row["analgesic"] == "TRUE":
        return "Pain Relief"
    else:
        return "Other"

df["Category"] = df.apply(classify_row, axis=1)

# ------------------------
# Save output
# ------------------------

df.to_excel("outputs/sample_output_classifications.xlsx", index=False)

print("Demo pipeline finished.")
