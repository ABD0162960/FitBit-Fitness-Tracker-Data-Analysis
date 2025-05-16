def checkSummaryStatistics(df):
    """
    Check summary statistics of the DataFrame.
    """
    print("Summary Statistics:")
    print(df.describe())
#     if file.endswith('.csv'):
#         print(f"Reading: {file}")
#         df = pd.read_csv(os.path.join(r'RawData\mturkfitbit_export_3.12.16-4.11.16\Fitabase Data 3.12.16-4.11.16', file))
#         print(df.info())
#         print("\n")


data_folders = [r'RawData\mturkfitbit_export_3.12.16-4.11.16\Fitabase Data 3.12.16-4.11.16', 
                r'RawData\mturkfitbit_export_4.12.16-5.12.16\Fitabase Data 4.12.16-5.12.16']

def checkStructure(df):
    """
    Check the structure of the DataFrame.
    """
    print("DataFrame Structure:")
    print(df.info())

def checkDataTypes(df):
    """
    Check the data types of the DataFrame.
    """
    print("Data Types:")
    print(df.dtypes)

def checkForDuplicates(df):
    """
    Check for duplicate rows in the DataFrame.
    """
    duplicates = df[df.duplicated()]
    if not duplicates.empty:
        print("⚠️ Duplicated rows found:")
        print(duplicates)
    else:
        print("✅ No duplicated rows found.")

def checkForMissingValues(df):
    """
    Check for missing values in the DataFrame.
    """
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("⚠️ Missing values found:")
        print(missing_values[missing_values > 0])
    else:
        print("✅ No missing values found.")

for folder in data_folders:
    for file in os.listdir(folder):
        if file.endswith('.csv'):
            print(f"Reading: {file}")
            df = pd.read_csv(os.path.join(folder, file))
            checkStructure(df)
            checkForDuplicates(df)
            checkForMissingValues(df)

            print("\n")  
