import pandas as pd

def read_records(file_path, filter_column=None, filter_value=None):
    """
    Read and optionally filter records from the Excel file.
    
    Args:
        file_path (str): Path to the Excel file.
        filter_column (str, optional): Column to filter on.
        filter_value (str/int, optional): Value to filter by.
        
    Returns:
        pd.DataFrame: The filtered or full dataset.
    """
    try:
        data = pd.read_excel(file_path)
    except FileNotFoundError:
        print("File not found. Make sure the database exists.")
        return None

    # Filter if needed
    if filter_column and filter_value:
        data = data[data[filter_column] == filter_value]
    
    print(data)
    return data
