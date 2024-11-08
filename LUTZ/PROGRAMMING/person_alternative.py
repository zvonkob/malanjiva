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

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, job='manager')
    # def giveRaise(self, percent, bonus=0.1):
        # self.pay *= (1. + percent + bonus) 
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith', 44)
    sue = Person('Sue Jones', 47, 40_000, 'hardware')
    tom = Manager(name='Tom Doe', age=50, pay=50_000)
    
    # print(sue)
    # print(sue.pay, sue.lastName())
    for obj in (bob, sue, tom):
        print()
        print(obj)
        obj.giveRaise(.10)
        print(obj)