from math import sqrt, cos, radians

def diagonala(a, gamma):
    '''
        cosine statement
        c**2 = a**2 + b**2 - 2*a*b*cos(gamma)
        where a = b
    '''
    c = a * sqrt(2 * (1 - cos(radians(gamma))))
    return round(c, 1)

def main():
    a = 4
    for eps in range(0, 35, 5):
        gamma = 90 - eps
        delta = 180 - gamma
        print('{:2d} deg = ({:.1f}, {:.1f}) cm'.format(
                eps, diagonala(a, gamma), diagonala(a, delta)))

main()

#  0 deg = (5.7, 5.7) cm
#  5 deg = (5.4, 5.9) cm
# 10 deg = (5.1, 6.1) cm
# 15 deg = (4.9, 6.3) cm
# 20 deg = (4.6, 6.6) cm
# 25 deg = (4.3, 6.7) cm
# 30 deg = (4.0, 6.9) cm