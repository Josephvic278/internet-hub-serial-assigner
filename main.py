import json
import os

# Get the current directory and construct the path to the JSON file
json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'internet_hubs.json')

# Load the JSON data from the file
with open(json_file_path, 'r') as file:
    internet_hubs_data = json.load(file)

# Function to assign serial numbers to internet hubs
def assign_serial_numbers(data):
    # Define the serial numbers range in reverse order
    reversed_serial_numbers = iter(range(1478, 1469, -1))  # 1478 to 1470 descending
    
    # Iterate over the hubs and assign serial numbers where needed
    for hub in data.get('Internet_hubs', []):
        # Only assign serial numbers to hubs with an ID starting with "mn"
        if hub['id'].startswith("mn"):
            hub['serial_number'] = f'C25CTW0000000000{next(reversed_serial_numbers)}'
    
    return data

# Update the hubs with serial numbers
updated_hubs_data = assign_serial_numbers(internet_hubs_data)

# Save the updated data back to a new JSON file
with open('clean_internet_hubs.json', 'w') as output_file:
    json.dump(updated_hubs_data, output_file, indent=4)