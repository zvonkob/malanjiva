from person import Person

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, job='manager')
    # def giveRaise(self, percent, bonus=0.1):
        # self.pay *= (1. + percent + bonus) 
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)
        
if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50_000)
    
    # print(tom.lastName())
    # tom.giveRaise(.20)
    # print(tom.pay)

    print(tom)
    