import csv
from typing import List

class CSVWriter:
    def write_to_csv(self, data: List[str], filename: str):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader() # Write column names
            writer.writerows(data)  # Write data rows