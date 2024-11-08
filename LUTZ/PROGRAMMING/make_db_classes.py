import shelve
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30_000, 'software')
sue = Person('Sue Jones', 47, 40_000, 'hardware')
tom = Manager('Tom Doe', 50, 50_000)

db = shelve.open('class-shelve')

db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

db.close()