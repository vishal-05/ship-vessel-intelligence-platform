import os
import zipfile
import requests

# NOAA verified direct archive link
URL = "https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2023/AIS_2023_01_01.zip"

RAW_DIR = os.path.join("data", "raw")
ZIP_PATH = os.path.join(RAW_DIR, "AIS_2023_01_01.zip")
TARGET_CSV = os.path.join(RAW_DIR, "ais_data.csv")


def download_and_extract():
    os.makedirs(RAW_DIR, exist_ok=True)

    print(f"📥 Downloading sample AIS dataset from NOAA...")
    response = requests.get(URL, stream=True)
    response.raise_for_status()

    with open(ZIP_PATH, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)

    print("📦 Extracting CSV...")
    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        # Extract files directly into data/raw/
        zip_ref.extractall(RAW_DIR)

    extracted_file = os.path.join(RAW_DIR, "AIS_2023_01_01.csv")
    if os.path.exists(extracted_file):
        if os.path.exists(TARGET_CSV):
            os.remove(TARGET_CSV)
        os.rename(extracted_file, TARGET_CSV)

    # Clean up the zip file to save disk space
    if os.path.exists(ZIP_PATH):
        os.remove(ZIP_PATH)

    print(f"✅ Success! AIS file ready at: {TARGET_CSV}")


if __name__ == "__main__":
    download_and_extract()