from models.data_generator import DataGenerator
from models.csv_writer import CSVWriter
import datetime
import sys

def main():
    column_names = [
        'Company', 'Product', 'Last Name', 'First Name', 'Telephone', 'Deal Status',
        'Completion Date', 'Sales Code', 'Type of Contact', 'Call Attempt #1', 'Call Attempt #2', 'Call Attempt #3',
        'Subscription Plan', 'Follow up', 'Type Of Contact', 'Last Name of Sales Rep',
        'First Name of Sales Rep', 'Title of Sales Rep', 'Comments'
    ]

    data_generator = DataGenerator(column_names)
    data = data_generator.generate_data(910)
    
    filename = sys.argv[1] 
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    outfile = filename + '_' + timestamp + '_.csv'
    directory = 'output/'
    
    csv_writer = CSVWriter()
    csv_writer.write_to_csv(data, directory + outfile)

if __name__ == '__main__':
    main()