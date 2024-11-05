def count_lines(f):
    f.seek(0)
    ll = f.readlines()
    return len(ll)

def count_chars(f):
    f.seek(0)
    # mm = [ch for ch in f.read()]
    mm = f.read()
    return len(mm)

def test(name):
    with open(name, 'r') as f:
        print('number of lines =', count_lines(f))
        print('number of chars =', count_chars(f))

if __name__ == '__main__':
    import sys
    print(sys.argv)
    if len(sys.argv) == 2:
        name = sys.argv[1]
    else:
        name = input('Input file name (.py) ')
    test(name + '.py')