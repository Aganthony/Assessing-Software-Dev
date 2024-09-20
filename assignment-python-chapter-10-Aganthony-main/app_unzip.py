from pathlib import Path
from zipfile import ZipFile


path = Path(".")
source_path = [p for p in path.iterdir() if p.is_dir()]

file_path = [p for p in path.rglob("*.zip")]
for file in file_path:
    with ZipFile(file) as zip:
        zip.extractall("worldbank_data")

print("All Files has been extracted from worldbank_zipfiles to worldbank_data")
