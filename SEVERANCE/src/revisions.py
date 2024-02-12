import re

PATTERN = 'New Revision: (\d+)'

fname = input('Enter file: ')
if len(fname) == 0:
    fname = 'mbox-short.txt'

ii = 0
sum = 0.

pth = '../data/' + fname
with open(pth, 'r') as f:
    for line in f:
        line = line.rstrip()
        matches = re.findall(PATTERN, line)
        for match in matches:
            ii += 1
            match = int(match)
            sum += match
            print(ii, match)


print(f'{sum / ii}')