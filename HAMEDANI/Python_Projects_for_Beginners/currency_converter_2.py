USD = 'USD'
EUR = 'EUR'
CAD = 'CAD'
CURRENCIES = (USD, EUR, CAD)
EUR_to_CAD = 1.4748
EUR_to_USD = 1.0507
USD_to_CAD = EUR_to_CAD / EUR_to_USD

while True:
    try:
        to_convert = float(input('Enter the amount: '))
        if to_convert < 0:
            raise ValueError()
        break
    except ValueError:
        print('Invalid amount')

while True:
    source_curr = input('Source currency (USD/EUR/CAD): ').upper()
    if source_curr in CURRENCIES:
        break
    else:
        print('Invalid currency')
    
while True:
    target_curr = input('Target currency (USD/EUR/CAD): ').upper()
    if target_curr in CURRENCIES:
        break
    else:
        print('Invalid currency')

exchange_rates = {}
exchange_rates[EUR] = {USD:     EUR_to_USD, CAD:     EUR_to_CAD}
exchange_rates[USD] = {EUR: 1 / EUR_to_USD, CAD:     USD_to_CAD}
exchange_rates[CAD] = {EUR: 1 / EUR_to_CAD, USD: 1 / USD_to_CAD}

if source_curr == target_curr:
    converted = to_convert
else:
    converted = exchange_rates[source_curr][target_curr] * to_convert

# to_convert = round(to_convert, 2)
converted = round(converted, 2)

print(f'{to_convert} {source_curr} is equal to {converted:.2f} {target_curr}')