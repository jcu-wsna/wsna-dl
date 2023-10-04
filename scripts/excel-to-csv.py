"""
  Open the excel file and sheet specified.
  Save all of the rows with Status == "Active" to the library-index.csv file.
"""
import pandas as pd

EXCEL_FILE = "./data/20230929_WSNA_Library.xlsx"
SHEET_NAME = "Repository"
OUTPUT_FILE_NAME = "./data/library-index.csv"

df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
active_records = df[df.Status == "Active"]
active_records.to_csv(
    OUTPUT_FILE_NAME, index=False
)  # index=False prevents pandas from writing a row index to the CSV.
