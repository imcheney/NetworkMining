def testDict(d):
    for key in d.keys():
        d[key] += 10
    return d

d1 = {'a':10, 'b':20}
testDict(d1)
print(d1)