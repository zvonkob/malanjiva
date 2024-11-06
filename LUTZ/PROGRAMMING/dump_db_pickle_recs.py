import pickle, glob


for filename in glob.glob('*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n', record)

print()    
suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])

print()
print(glob.glob('*.pkl'))