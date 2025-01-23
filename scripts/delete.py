import pandas as pd

def delete_record(file_path, filter_column, filter_value):
    """
    Delete records from the Excel file based on a filter condition.
    
    Args:
        file_path (str): Path to the Excel file.
        filter_column (str): Column to filter on.
        filter_value (str/int): Value to delete records by.
        
    Returns:
        None
    """
    try:
        data = pd.read_excel(file_path)
    except FileNotFoundError:
        print("File not found. Make sure the database exists.")
        return None

    # Filter out rows that match the condition
    updated_data = data[data[filter_column] != filter_value]
    updated_data.to_excel(file_path, index=False)
    print(f"Records where {filter_column} = {filter_value} have been deleted.")
