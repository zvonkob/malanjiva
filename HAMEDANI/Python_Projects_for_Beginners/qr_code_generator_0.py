import qrcode


data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename: ').strip()

img = qrcode.make(data)

img.save(filename)

print(f'QR Code saved to {filename}')
