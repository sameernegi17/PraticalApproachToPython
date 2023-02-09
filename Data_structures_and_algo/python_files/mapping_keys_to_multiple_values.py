d = {
 'a' : [1, 2, 3,3],
 'b' : [4, 5]
}
e = {
 'a' : {1, 2, 3,3},
 'b' : {4, 5}
}

#print(d,e)


#Default Dict Example
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
#print(d)


d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
#print(d)

# Why Default Dict oVer normal Dict

from collections import defaultdict
pairs = (("a",2),("a",3),("b",5))

d = {}
for key, value in pairs:
  if key not in d:
    d[key] = []
  d[key].append(value)

print(d)
#Using a defaultdict simply leads to much cleaner code:

d = defaultdict(list)
for key, value in pairs:
 d[key].append(value)

print(d)






