import os


def main():
    file_name = input('Enter the filename to open or create: ').strip()
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                content = file.read()
                print(content)
        else:
            with open(file_name, 'w') as file:
                pass
    except OSError:
        print(f'{file_name} could not be opened.')
        return
    
    print('\nEnter your text (type SAVE on a new line to save and exit)')
    content = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        content.append(line)

    try:
        with open(file_name, 'w') as file:
            file.write('\n'.join(content))
            print(f'{file_name} saved.')
    except OSError:
        print(f'{file_name} could not be saved.')
        return
    

if __name__ == '__main__':
    main()