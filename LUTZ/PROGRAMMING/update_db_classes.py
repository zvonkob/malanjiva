import shelve

db = shelve.open('class-shelve')

sue = db['sue']
sue.giveRaise(.1)
db['sue'] = sue 

tom = db['tom']
tom.giveRaise(.2)
db['tom'] = tom

db.close()