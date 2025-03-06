import gspread
from google.oauth2.service_account import Credentials
from random import shuffle
import time
from gspread.exceptions import SpreadsheetNotFound, APIError

# The scope of the Google Sheet we are accessing
SCOPE = ['https://www.googleapis.com/auth/spreadsheets']

try:
    # Load credentials and authorize client
    creds = Credentials.from_service_account_file('creds.json', scopes=SCOPE)
    client = gspread.authorize(creds)

    # Open the Google Sheet by its ID
    sheet_id = 'your_google_sheet_id_here'
    workbook = client.open_by_key(sheet_id)

    print(f"Successfully accessed sheet: {workbook.title}")

    # Get the worksheet
    sheet = workbook.worksheet('Sheet1')

    # Function to shuffle non-empty elements in the sheet
    def shuffle_non_empty_elements(sheet):
        # Get all values from the sheet
        all_values = sheet.get_all_values()
        
        # Flatten the list of lists into a single list and filter out empty cells
        flat_values = [item for sublist in all_values for item in sublist if item.strip()]
        
        # Shuffle the flat list of non-empty values
        shuffle(flat_values)
        
        # Replace the original non-empty values with the shuffled ones
        index = 0
        for i in range(len(all_values)):
            for j in range(len(all_values[i])):
                if all_values[i][j].strip():  # Only replace non-empty cells
                    all_values[i][j] = flat_values[index]
                    index += 1
        
        # Update the sheet with the shuffled values
        for i in range(len(all_values)):
            sheet.update(f'A{i+1}', [all_values[i]])
            time.sleep(1)  # Add a delay of 1 second between each write request

    # Function to change all elements to a specified string
    def change_all_elements(sheet, new_value):
        # Get all values from the sheet
        all_values = sheet.get_all_values()
        
        # Replace all non-empty cells with the new value
        for i in range(len(all_values)):
            for j in range(len(all_values[i])):
                if all_values[i][j].strip():  # Only replace non-empty cells
                    all_values[i][j] = new_value
        
        # Update the sheet with the new values
        for i in range(len(all_values)):
            sheet.update(f'A{i+1}', [all_values[i]])
            time.sleep(1)  # Add a delay of 1 second between each write request

    # Main loop
    while True:
        user_input = input("Enter 'shuffle' to shuffle elements or enter a string to replace all elements: ").strip()
        
        if user_input.lower() == 'shuffle':
            print("Shuffling elements in the sheet...")
            shuffle_non_empty_elements(sheet)
        else:
            print(f"Changing all elements to '{user_input}'...")
            change_all_elements(sheet, user_input)
        
        updated_values = sheet.get_all_values()
        for row in updated_values:
            print(row)

except FileNotFoundError:
    print("Error: The 'creds.json' file was not found.")
except SpreadsheetNotFound:
    print("Error: The Google Sheet was not found.")
except APIError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")