import json
from datetime import datetime

def update_data_json():
  """
  Updates data.json with the current date and time.

  - Reads existing data (if any) from data.json.
  - Gets the current date and time in a format suitable for JSON.
  - Creates a new dictionary with the existing data and the timestamp.
  - Writes the updated dictionary to data.json.
  """

  try:
    with open('data.json', 'r') as f:
      existing_data = json.load(f)
  except FileNotFoundError:
    existing_data = {}  # Empty dictionary if data.json doesn't exist

  current_datetime = str(datetime.now().strftime("%H:%M %d/%m/%Y")) # Use ISO 8601 format for consistency

  updated_data = {**existing_data, "subheading": current_datetime}

  with open('data.json', 'w') as f:
    json.dump(updated_data, f, indent=2)  # Indent for readability

if __name__ == '__main__':
  update_data_json()
  print("Data.json updated successfully!",str(datetime.now().strftime("%H:%M %d/%m/%Y")))
