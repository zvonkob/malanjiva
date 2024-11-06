import sys


dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def storeDbase(db, dbfilename=dbfilename):
    
    "formated dump of database to flat file"
    if dbfilename == None:
        dbfile = sys.stdout
    else:
        dbfile = open(dbfilename, 'w')
    for key, rec in db.items():
        print(key, file=dbfile)
        for name, value in rec.items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()

def loadDbase(dbfilename=dbfilename):
    "parse data to reconstruct database"
    dbfile = open(dbfilename, 'r')
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db

    
if __name__ == '__main__':
    # from initdata import db
    # storeDbase(db, 'file01.txt')
    #
    # db = loadDbase('file01.txt')
    # storeDbase(db, 'file02.txt')
    #
    db = loadDbase('file02.txt')
    storeDbase(db, dbfilename=None)