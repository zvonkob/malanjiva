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
    def __str__(self):
        rez = f'<{self.__class__.__name__:s} => {self.name:s}>'
        for att, value in self.__dict__.items():
            rez += f'\n        {att} => {value}'
        return rez
    def __add__(self, percent):
        self.giveRaise(percent)
        return self
        

if __name__ == '__main__':
    
    bob = Person('Bob Smith', 42, 30_000, 'software')
    # sue = Person('Sue Jones', 45, 40_000, 'hardware')
    
    # print(bob.name, sue.pay)
    # print(bob.lastName())
    # sue.giveRaise(.10)
    # print(sue.pay)
    
    print(bob)
    
    bob += 0.20
    
    print(bob)
    
    # print(sue)
   
    