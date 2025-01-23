import unittest
import pandas as pd
from scripts.create import create_record

class TestCreateRecord(unittest.TestCase):
    def test_create_record(self):
        # Create a temporary Excel file
        file_path = "data/temp_test.xlsx"
        new_record = {"ID": 1, "Name": "Test User", "Email": "test@example.com", "Phone": "123-456"}
        
        # Run the create function
        create_record(file_path, new_record)
        
        # Read the file and verify the record
        data = pd.read_excel(file_path)
        self.assertEqual(len(data), 1)
        self.assertEqual(data.loc[0, "Name"], "Test User")

if __name__ == "__main__":
    unittest.main()
