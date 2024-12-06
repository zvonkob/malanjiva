USD = 'USD'
EUR = 'EUR'
CAD = 'CAD'
CURRENCIES = {USD, EUR, CAD}
EUR_to_CAD = 1.4748
EUR_to_USD = 1.0507
USD_to_CAD = EUR_to_CAD / EUR_to_USD

while True:
    try:
        to_convert = float(input('Enter the amount: '))
    except ValueError:
        print('Invalid amount')
        continue
    if to_convert > 0:
        break
    else:
        print('Invalid amount')

while True:
    source_curr = input('Source currency (USD/EUR/CAD): ').upper().strip()
    if source_curr in CURRENCIES:
        break
    else:
        print('Invalid currency')
    
while True:
    target_curr = input('Target currency (USD/EUR/CAD): ').upper().strip()
    if target_curr in CURRENCIES:
        break
    else:
        print('Invalid currency')

if source_curr == EUR and target_curr == USD:
    converted = EUR_to_USD * to_convert
elif source_curr == USD and target_curr == EUR:
    converted = (1 / EUR_to_USD) * to_convert
elif source_curr == EUR and target_curr == CAD:
    converted = EUR_to_CAD * to_convert
elif source_curr == CAD and target_curr == EUR:
    converted = (1 / EUR_to_CAD) * to_convert
elif source_curr == USD and target_curr == CAD:
    converted = USD_to_CAD * to_convert
else:
    converted = (1 / USD_to_CAD) * to_convert

to_convert = round(to_convert, 2)
converted = round(converted, 2)

print(f'{to_convert:.2f} {source_curr} is equal to {converted:.2f} {target_curr}')