import re


def grep(pattern):
    ii = 0
    with open('../data/mbox.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            matches = re.findall(pattern, line)
            if len(matches) > 0:
                ii += 1
                match = matches[0]
    return f'mbox.txt had {ii} lines that matched {pattern}'


if __name__ == '__main__':
    pattern = input('Enter a regular expression: ')
    res = grep(pattern)
    print(res)
