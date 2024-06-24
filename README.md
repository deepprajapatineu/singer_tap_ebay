# Singer Tap eBay

## Overview
This project, **Singer Tap eBay**, is designed to extract financial payout data from eBay's General Ledger API. It processes and saves the data both as CSV files and directly into Google Sheets.

## Prerequisites
- Python 3.7+
- Access to eBay's General Ledger API
- A Google Cloud project with a configured service account
- Google Sheets API enabled in your Google Cloud project

## Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/singer_tap_eBay.git
cd singer_tap_eBay
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Google Credentials
Create a service account in your Google Cloud Console and download the JSON key file. Place it within the config directory and rename it to googlecreds.json.

### Configure Application
Edit the config/config.json file to include your eBay bearer token and Google Sheets details.

### Obtaining eBay API Credentials
To access eBay's General Ledger API, you need an OAuth `bearer_token`:

1. **Register an application** on the eBay Developer Program website to get your client credentials.
2. **Follow eBay's OAuth client credentials grant flow** to obtain a bearer token.
3. **Securely store the bearer token** in the `config/config.json` file.

For detailed instructions on eBay API authentication, visit below links: 
1. [eBay OAuth documentation](https://developer.ebay.com/api-docs/static/oauth-client-credentials-grant.html)
2. [Finances API Release documentation](https://developer.ebay.com/api-docs/sell/finances/release-notes.html)


### Usage
Run the script with:
```bash
python main.py
```
OR
```bash
--config config.json --catalog catalog.json
```

### Output
CSV files will be stored in the output/ directory.
Data will be written to the specified Google Sheets.
