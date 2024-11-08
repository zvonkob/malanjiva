import shelve

db = shelve.open('class-shelve')

for key in db:
    print(key, '=>\n', db[key].name, db[key].pay)

print()
bob = db['bob']
print(bob.lastName())

print()
print(db['tom'].lastName())

db.close()
