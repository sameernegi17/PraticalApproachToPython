"""
Matching Strings Using Shell Wildcard Patterns
"""

from fnmatch import fnmatch,fnmatchcase

print(fnmatch("foo.txt","*txt"))
print(fnmatch("foo.txt","?oo.txt"))
print(fnmatch("saoo.txt","?oo.txt"))

print("Dat54.txt" , fnmatch("Dat54.txt","Dat[0-9][0-9]*"))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

print("names",[name for name in names if fnmatch(name, "Dat*.csv")])

addresses = [
 '5412 N CLARK ST',
 '1060 W ADDISON ST',
 '1039 W GRANVILLE AVE',
 '2122 N CLARK ST',
 '4802 N BROADWAY',
]

print("Address",[name for name in addresses if fnmatchcase(name, "* ST")])