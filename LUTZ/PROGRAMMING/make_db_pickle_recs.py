from initdata import bob, sue, tom
import pickle


for key, record in [('bob', bob), ('sue', sue), ('tom', tom)]:
    with open(key + '.pkl', 'wb') as dbfile:
        pickle.dump(record, dbfile)