import xml.etree.ElementTree as ET
import csv

# Function to parse the XML file and extract the relevant data
def parse_apple_health_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Define a list to store the data
    records = []
    
    # Iterate through all 'Record' elements in the XML file
    for record in root.findall('.//Record'):
        # Extract the relevant attributes from each 'Record' element
        record_data = {
            'type': record.get('type'),  # Data type (e.g., "HKQuantityTypeIdentifierStepCount")
            'sourceName': record.get('sourceName'),  # Source (e.g., the device or app)
            'sourceVersion': record.get('sourceVersion'),  # Version of the source
            'unit': record.get('unit'),  # Unit of the measurement (e.g., "count", "mg/dL")
            'value': record.get('value'),  # The value of the record (e.g., "100" steps)
            'startDate': record.get('startDate'),  # Start date of the record (e.g., '2024-01-01 12:00:00')
            'endDate': record.get('endDate'),  # End date of the record (e.g., '2024-01-01 12:30:00')
        }
        
        # Append the record to the list
        records.append(record_data)
    
    return records

# Function to write the data to a CSV file
def write_to_csv(records, csv_file):
    # Open a new CSV file for writing
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=records[0].keys())
        
        # Write the header (fieldnames)
        writer.writeheader()
        
        # Write the records to the CSV file
        writer.writerows(records)

# Main function to convert the Apple Health XML to CSV
def convert_xml_to_csv(xml_file, csv_file):
    # Parse the XML file
    records = parse_apple_health_xml(xml_file)
    
    # If there are records to write, proceed to write them to CSV
    if records:
        write_to_csv(records, csv_file)
        print(f"Data successfully converted to {csv_file}")
    else:
        print("No records found in the XML file.")

# Example usage
xml_file = 'export.xml'  # Path to your Apple Health export XML file
csv_file = 'apple_health_data.csv'   # Path to the output CSV file

# Convert the XML file to CSV
convert_xml_to_csv(xml_file, csv_file)
