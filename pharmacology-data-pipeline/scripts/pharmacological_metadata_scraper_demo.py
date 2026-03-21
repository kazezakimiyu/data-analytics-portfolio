"""
Pharmacological Metadata Extraction (Demo Version)

This script demonstrates how additional compound metadata
(e.g., pharmacodynamics, classification labels) can be extracted
from PubChem.

Note:
This is a simplified version for demonstration purposes only.
"""

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ------------------------
# Setup driver
# ------------------------

def init_driver():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)

# ------------------------
# Scraping function
# ------------------------

def extract_metadata(compound_name):
    driver = init_driver()

    try:
        driver.get("https://pubchem.ncbi.nlm.nih.gov/")
        search_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        search_box.send_keys(compound_name)
        search_box.submit()

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        pharmacodynamics = "Not found"
        if soup.find(string=lambda t: "pharmacology" in str(t).lower()):
            pharmacodynamics = "Detected"

        return {
            "Pharmacodynamics": pharmacodynamics,
            "ATC_Code": "Sample"
        }

    except Exception as e:
        return {
            "Pharmacodynamics": "Error",
            "ATC_Code": "Error"
        }

    finally:
        driver.quit()

# ------------------------
# Load input
# ------------------------

df = pd.read_excel("inputs/sample_substances.xlsx")

# ------------------------
# Apply extraction
# ------------------------

results = df["Compound_Name"].apply(extract_metadata)
results_df = pd.DataFrame(list(results))

df = pd.concat([df, results_df], axis=1)

# ------------------------
# Save output
# ------------------------

df.to_excel("outputs/sample_metadata_output.xlsx", index=False)

print("Metadata extraction demo complete.")
