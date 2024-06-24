import json
from src.api import get_data
from src.sheets import initialize_sheets_service, write_data_to_google_sheets
from src.csv_handler import write_data_to_csv 

# Load configuration settings from file.
def load_config():
    with open('config/config.json') as f:
        return json.load(f)

# Main function to execute the workflow.
def main():
    
    config = load_config()
    data = get_data(config["bearer_token"])
    
    if "payouts" in data:
        # write data in CSV format
        write_data_to_csv(data["payouts"], 'output/payouts.csv')

        # Initialization of Google Sheets and write data
        sheet_service = initialize_sheets_service("./config/googlecreds.json")
        write_data_to_google_sheets(sheet_service, data["payouts"], config["spreadsheet_id"], "data!A1")
        print("Data is successfully stored in the Google Sheet!")

if __name__ == "__main__":
    main()
