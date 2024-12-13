''' Utility module za delo s časom.  '''
from datetime import datetime, timedelta


'''
Seštevanje dolžine videotov
'''


def main():
    '''glavni program'''
    tt = timedelta()
    while True:
        res = input('Minutes:Seconds ')
        min, sec = res.split()
        t = timedelta(minutes=int(min), seconds=int(sec))
        tt += t
        print(t, tt)


if __name__ == '__main__':
    main()
