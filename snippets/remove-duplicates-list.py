a = [1,"1",2,"1"]

#using set
print(list(set(a)))

#using collections
from collections import OrderedDict
a = list(OrderedDict.fromkeys(a))
print(a)

#normal way
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
