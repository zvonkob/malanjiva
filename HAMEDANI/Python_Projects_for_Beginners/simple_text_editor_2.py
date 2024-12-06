from os.path import *

def main():
    file_name = input('Enter the file_name to open or create: ').strip()
    if exists(file_name):
        try:
            f = open(file_name, 'r')
        except PermissionError:
            print(f'{file_name} could not be opened')
            return
        for line in f:
            print(line.rstrip())
        f.close()

    print('\nEnter your text (type SAVE on a new line to save and exit)')
    lines = []
    while True:
        line = input()
        lines.append(line)
        if line.strip() == 'SAVE':
            break
    
    with open(file_name, 'w') as g:
        for line in lines:
            g.write(f'{line}\n')

if __name__ == '__main__':
    main()