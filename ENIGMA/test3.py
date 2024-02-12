# def some1(x):
    # for ii in range(3):
        # print(ii, x)

# some1('Zvonko1')


# print(dir(some1))

# print()
# print('some1.__code__ =')
# print(dir(some1.__code__))


# print()
# print('some1.__code__.co_varnames =')
# print(some1.__code__.co_varnames)

# print()
# print('some1.__code__.co_lines =')
# print(dir(some1.__code__.co_lines))




def f(x):
    y = 42
    l = locals()
    # print(type(l))
    print(", ".join(["{var}: {type}".format(var=v, type=type(l[v])) for v in l]))
    print(l)
    
    
# print()
# print(f.__code__.co_varnames)


# print()
# print()
# print()
# print(some1.__code__.co_varnames)
# print(some1.__code__.co_varnames)

f(32)

print(f.__code__.co_varnames)