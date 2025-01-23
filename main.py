from scripts.create import create_record
from scripts.read import read_records
from scripts.update import update_record
from scripts.delete import delete_record

FILE_PATH = "data/database.xlsx"

# Example data
new_record = {"ID": 1, "Name": "John Doe", "Email": "john@example.com", "Phone": "123-456-7890"}

# Create a new record
create_record(FILE_PATH, new_record)

# Read all records
read_records(FILE_PATH)

# Update a record
update_record(FILE_PATH, row_index=0, column_name="Name", new_value="Jane Doe")

# Delete a record
delete_record(FILE_PATH, filter_column="ID", filter_value=1)

# Read records again to verify
read_records(FILE_PATH)
