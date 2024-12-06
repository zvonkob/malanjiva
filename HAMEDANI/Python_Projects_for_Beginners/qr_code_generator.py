import qrcode


text_URL = input('Enter the text or URL: ')
file_text_URL = input('Enter the filename: ')

img = qrcode.make(text_URL)

img.save(file_text_URL)

print(f'QR Code saved to {file_text_URL}')
