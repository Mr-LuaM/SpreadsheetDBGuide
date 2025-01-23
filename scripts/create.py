import pandas as pd

def create_record(file_path, new_record):
    """
    Add a new record to the Excel file.
    
    Args:
        file_path (str): Path to the Excel file.
        new_record (dict): A dictionary representing the new record to add.
        
    Returns:
        None
    """
    try:
        # Load existing data
        data = pd.read_excel(file_path)
    except FileNotFoundError:
        # If file doesn't exist, create a new one with columns based on the new record
        data = pd.DataFrame(columns=new_record.keys())
    
    # Append the new record
    new_data = pd.DataFrame([new_record])
    updated_data = pd.concat([data, new_data], ignore_index=True)
    
    # Save back to Excel
    updated_data.to_excel(file_path, index=False)
    print(f"Record added successfully: {new_record}")
