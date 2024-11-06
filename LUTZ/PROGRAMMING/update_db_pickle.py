import pickle

with open('people-pickle', 'rb') as dbfile:
    db = pickle.load(dbfile)

db['sue']['pay'] *= 1.20
db['tom']['name'] = 'Tom Tom Tom'

with open('people-pickle', 'wb') as dbfile:
    pickle.dump(db, dbfile)



