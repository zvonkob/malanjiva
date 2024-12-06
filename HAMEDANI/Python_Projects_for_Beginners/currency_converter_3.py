USD = 'USD'
EUR = 'EUR'
CAD = 'CAD'

def get_amount():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount < 0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid amount')

def get_currency(label):
    CURRENCIES = (USD, EUR, CAD)
    while True:
        currency = input(f'{label} currency (USD/EUR/CAD): ').upper()
        if currency in CURRENCIES:
            return currency
        else:
            print('Invalid currency')
    
def convert(amount, source_curr, target_curr):
    EUR_to_CAD = 1.4748
    EUR_to_USD = 1.0507
    USD_to_CAD = EUR_to_CAD / EUR_to_USD
    exchange_rates = {
        EUR: {USD:     EUR_to_USD, CAD:     EUR_to_CAD},
        USD: {EUR: 1 / EUR_to_USD, CAD:     USD_to_CAD},
        CAD: {EUR: 1 / EUR_to_CAD, USD: 1 / USD_to_CAD}
    }
    if source_curr == target_curr:
        return to_convert
    
    return exchange_rates[source_curr][target_curr] * amount

def main():
    to_convert = get_amount()
    source_curr = get_currency('Source')
    target_curr = get_currency('Target')
    converted = convert(to_convert, source_curr, target_curr)

    print(f'{to_convert} {source_curr} is equal to {converted:.2f} {target_curr}')

if __name__ == '__main__':
    main()