from pathvalidate import validate_filename

while True:
    filename = input('Enter the filename to open or create: ')
    try:
        validate_filename(filename=filename, platform='Windows')
        break
    except ValueError:
        print(f'{filename} not a valid Windows filename')

# lines = []
# while True:
#     line = input()
#     if 
# m    lines.app
# try:
#     f = open(filename, 'r')
# except FileNotFoundError:
    
# except PermissionError:
#    print(f'{filename} could not be opened')
