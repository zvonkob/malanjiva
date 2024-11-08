
# initalize data to be stored in files, pickles, shelves

# records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

print(f'\nThis module (initdata) is being run by the: {__name__:s} module.\n')

if __name__ == '__main__':
    print('Module initdata is used as a program.\n')
    for key in db:
        print(key, '=>\n  ', db[key])
else:
    print('Module initdata is used as a library.\n')
