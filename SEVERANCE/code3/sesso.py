class PartyAnimal:
    x = 0
    def party(self):
        self.x += 1
        print('So far', self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
print(dir(an))
print(type(an))