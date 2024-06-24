import requests

def get_data(bearer_token):
    url = "https://apiz.sandbox.ebay.com/sell/finances/v1/payout"
    headers = {"Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
