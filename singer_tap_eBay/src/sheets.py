from google.oauth2 import service_account
from googleapiclient.discovery import build

def initialize_sheets_service(credentials_file):
    credentials = service_account.Credentials.from_service_account_file(credentials_file)
    service = build('sheets', 'v4', credentials=credentials)
    return service.spreadsheets()

def write_data_to_google_sheets(sheet_service, data, spreadsheet_id, range_name):
    values = [create_headers()] + [flatten_data(item) for item in data]
    body = {'values': values}
    sheet_service.values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption="RAW",
        body=body
    ).execute()

def create_headers():
    return [
        'Payout ID', 'Payout Status', 'Payout Status Description', 'Amount Value',
        'Amount Currency', 'Payout Date', 'Last Attempted Payout Date', 'Transaction Count',
        'Instrument Type', 'Nickname', 'Account Last Four Digits'
    ]

def flatten_data(item):
    return [
        item.get('payoutId', ''),
        item.get('payoutStatus', ''),
        item.get('payoutStatusDescription', ''),
        item.get('amount', {}).get('value', ''),
        item.get('amount', {}).get('currency', ''),
        item.get('payoutDate', ''),
        item.get('lastAttemptedPayoutDate', ''),
        item.get('transactionCount', ''),
        item.get('payoutInstrument', {}).get('instrumentType', ''),
        item.get('payoutInstrument', {}).get('nickname', ''),
        item.get('payoutInstrument', {}).get('accountLastFourDigits', '')
    ]
