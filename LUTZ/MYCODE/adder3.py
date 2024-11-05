def adder(*kargs):
    res = kargs[0]
    for karg in kargs[1:]:
        res += karg
    return res

a = adder('Katarina', 'Barbara', 'Suzana')
print(a)

a = adder(list(range(10)), list(range(20, 25)))
print(a)

a = adder(3.13, 0.01)
print(a)
