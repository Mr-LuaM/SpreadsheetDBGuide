import pandas as pd

def update_record(file_path, row_index, column_name, new_value):
    """
    Update a specific value in the Excel file.
    
    Args:
        file_path (str): Path to the Excel file.
        row_index (int): Index of the row to update.
        column_name (str): Column to update.
        new_value (str/int): New value to set.
        
    Returns:
        None
    """
    try:
        data = pd.read_excel(file_path)
    except FileNotFoundError:
        print("File not found. Make sure the database exists.")
        return None

    if row_index in data.index:
        data.loc[row_index, column_name] = new_value
        data.to_excel(file_path, index=False)
        print(f"Record updated successfully at row {row_index}, column {column_name}.")
    else:
        print("Row index not found.")
