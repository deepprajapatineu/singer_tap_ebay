import csv

def write_data_to_csv(data, filename):

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = [
            'payoutId', 'payoutStatus', 'payoutStatusDescription', 'amount_value',
            'amount_currency', 'payoutDate', 'lastAttemptedPayoutDate', 'transactionCount',
            'payoutInstrument_instrumentType', 'payoutInstrument_nickname', 'payoutInstrument_accountLastFourDigits'
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in data:
            writer.writerow({
                'payoutId': item.get('payoutId', ''),
                'payoutStatus': item.get('payoutStatus', ''),
                'payoutStatusDescription': item.get('payoutStatusDescription', ''),
                'amount_value': item.get('amount', {}).get('value', ''),
                'amount_currency': item.get('amount', {}).get('currency', ''),
                'payoutDate': item.get('payoutDate', ''),
                'lastAttemptedPayoutDate': item.get('lastAttemptedPayoutDate', ''),
                'transactionCount': item.get('transactionCount', ''),
                'payoutInstrument_instrumentType': item.get('payoutInstrument', {}).get('instrumentType', ''),
                'payoutInstrument_nickname': item.get('payoutInstrument', {}).get('nickname', ''),
                'payoutInstrument_accountLastFourDigits': item.get('payoutInstrument', {}).get('accountLastFourDigits', '')
            })
    print("Your data is successfully saved at output -> payouts.csv ")
