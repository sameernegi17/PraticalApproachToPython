"""
Naming a Slice

Your program has become an unreadable mess of hardcoded slice indices and you want
to clean it up.
"""

record = "....................100.......513.25.........."
cost = int(record[20:23]) * float(record[30:36])
print("cost1",cost)

SHARE = slice(20,23)
COST = slice(30,36)

cost = int(record[SHARE]) * float(record[COST])
print("cost2",cost)


items = [0, 1, 2, 3, 4, 5, 6]

a = slice(2,4)

print(items[a])

items[a] = (10,11)
print(items)

del items[a]
print(items)


print(a.start)
print(a.stop)
print(a.step)

a = slice(5,50,2)

s = "Hello World"

print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
   print(s[i])