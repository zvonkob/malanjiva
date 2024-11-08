class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1. + percent)
    # def __str__(self):
        # return f'<{self.__class__.__name__:s} => {self.name:s}>'
    def __str__(self):
        for att in self.__class__.__dict__:
            print(att)

if __name__ == '__main__':
    
    bob = Person('Bob Smith', 42, 30_000, 'software')
    sue = Person('Sue Jones', 45, 40_000, 'hardware')
    
    # print(bob.name, sue.pay)
    
    # print(bob.lastName())
    
    # sue.giveRaise(.10)
    # print(sue.pay)
    
    # print()
    # for person in [bob, sue]:
        # print(person)
    
    print(bob)
   
    