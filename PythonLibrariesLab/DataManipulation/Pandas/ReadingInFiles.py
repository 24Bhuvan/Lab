import pandas as pd

# =====================
# SECTION 1: read_csv()
# =====================

# filepath_or_buffer: Path to CSV file or URL
csv_path = "data.csv"

# sep: Delimiter (default=',')
df = pd.read_csv(csv_path, sep=",")

# header: Row number(s) to use as column names (default=0)
df = pd.read_csv(csv_path, header=0)

# names: Custom column names (use header=None to ignore default header)
df = pd.read_csv(csv_path, names=["col1", "col2", "col3"], header=None)

# index_col: Set a column as index
df = pd.read_csv(csv_path, index_col=0)

# usecols: Load only selected columns
df = pd.read_csv(csv_path, usecols=["col1", "col3"])

# dtype: Specify data type of columns
df = pd.read_csv(csv_path, dtype={"col1": int, "col2": float})

# na_values: Additional strings to recognize as NaN
df = pd.read_csv(csv_path, na_values=["NA", "Missing"])

# parse_dates: Convert columns to datetime
df = pd.read_csv(csv_path, parse_dates=["date_col"])

# encoding: Specify file encoding (useful for non-UTF8 files)
df = pd.read_csv(csv_path, encoding="utf-8")


# =====================
# SECTION 2: read_excel()
# =====================

excel_path = "data.xlsx"

# io: Path to Excel file or ExcelFile object
df_xl = pd.read_excel(excel_path)

# engine: Backend engine (openpyxl, xlrd, etc.)
df_xl = pd.read_excel(excel_path, engine="openpyxl")

# sheet_name: Load specific sheet by name or index
df_xl = pd.read_excel(excel_path, sheet_name="Sheet1")
df_xl2 = pd.read_excel(excel_path, sheet_name=0)

# NOTE: The following args behave same as in read_csv():
# header, names, index_col, dtype, na_values, parse_dates, usecols


# =====================
# SECTION 3: Other Pandas Functions
# =====================

# set_option: Configure display options
pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 20)

# info(): Summary of DataFrame (columns, dtypes, non-null counts)
print(df.info())

# shape: Returns (rows, columns)
print(df.shape)

# head(): First n rows (default 5)
print(df.head())

# tail(): Last n rows (default 5)
print(df.tail())

# loc: Label-based indexing
print(df.loc[0, "col1"])       # single value
print(df.loc[0:3, ["col1"]])   # multiple rows + specific column

# iloc: Integer position-based indexing
print(df.iloc[0, 1])           # single value
print(df.iloc[0:3, 0:2])       # multiple rows & cols