from os.path import *

def show_file():
    file_name = input('Enter the file_name to open or create: ').strip()
    if exists(file_name):
        try:
            f = open(file_name, 'r')
        except PermissionError:
            print(f'{file_name} could not be opened')
            return False, file_name
        for line in f:
            print(line.rstrip())
        f.close()
    return True, file_name

def edit_file():
    print('\nEnter your text (type SAVE on a new line to save and exit)')
    lines = []
    while True:
        line = input()
        if line.strip() == 'SAVE':
            break
        lines.append(line)
    return lines

def write_file(lines, file_name):
    with open(file_name, 'w') as g:
        for line in lines:
            g.write(f'{line}\n')

def main():
    res, file_name = show_file()
    if not res: return

    lines = edit_file()

    write_file(lines, file_name)

if __name__ == '__main__':
    main()