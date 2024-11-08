import shelve

from person import Person

fieldnames = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    
    if not key:
        break
    if key in db:
        obj_record = db[key]
    else:
        obj_record = Person(name='?', age='?')

    for field in fieldnames:
        curr_val = getattr(obj_record, field)
        
        new_text = input(f'\t[{field}] = {curr_val}\n\t\tnew? => ')
        
        if new_text:
            setattr(obj_record, field, eval(new_text))
    db[key] = obj_record
db.close()
            