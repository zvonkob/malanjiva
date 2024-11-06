import pickle


suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
print()
print(sue)
suefile.close()

sue['pay'] *= 1.10

print(sue)

suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()