l1 = list(range(1, 1001))
print(l1)

def times10(x):
    return x * 10

'''
for x in l1:
    print(times10(x))
'''

#print(list(map(times10, l1)))
print(list(map(lambda x : x * 10, l1)))