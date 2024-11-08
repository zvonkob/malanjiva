import shelve

db = shelve.open('people-shelve')

for key in db:
    print(key, '=>', db[key])

print()
print(db['sue']['name'])
print()

db.close()