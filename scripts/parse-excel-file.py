"""  parse-excel-file.py

  Open the excel file and sheet specified.
  Save all of the rows with Status == "Active" to the library-index.csv file.
  Save the config information (1st 3 rows) as separate csv files.

"""
import pandas as pd

# inputs
EXCEL_FILE = "./inputs/library-index.xlsx"
SHEET_NAME = "Repository"

# outputs
FILTER_CONFIG = "./outputs/filter-config.csv"
SEARCH_CONFIG = "./outputs/search-config.csv"
DOC_DISPLAY_CONFIG = "./outputs/doc-display-config.csv"
DOC_LIB_INDEX = "./outputs/library-index.csv"

# Save only the Active records in the document library index
# Note: index=False prevents pandas from writing a row index to the CSV.
df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME, header=3)
active_records = df[df.Status == "Active"]
active_records.to_csv(DOC_LIB_INDEX, index=False)

# Extract the config data rows and save them as separate CSV files
col_labels = df.columns  # use column labels from previous load of this file
df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME, header=None)
df.columns = col_labels

filter_data = (
    df.iloc[[0]]
    .replace({"Filter_yes": True, "Filter_no": False})
    .to_csv(FILTER_CONFIG, index=False)
)
search_data = (
    df.iloc[[1]]
    .replace({"Search_yes": True, "Search_no": False})
    .to_csv(SEARCH_CONFIG, index=False)
)
full_display_data = (
    df.iloc[[2]]
    .replace({"FullDisplay_yes": True, "FullDisplay_no": False})
    .to_csv(DOC_DISPLAY_CONFIG, index=False)
)
