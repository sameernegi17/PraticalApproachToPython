"""
Transforming and Reducing Data at the Same Time

You need to execute a reduction function (e.g., sum(), min(), max()), but first need to
transform or filter the data
"""

nums = [1,2,3,4]

print(sum(x*x for x in nums))

import os

files = os.listdir(".")

if any(names.endswith(".py") for names in files):
    print("There is a py file")
else:
    print("no py file")

# Create a csv file
s = ("ACME",50,123.56)

print(",".join(str(x) for x in s))

# Data reduction across fields of a data structure

portfolio = [
 {'name':'GOOG', 'shares': 50},
 {'name':'YHOO', 'shares': 75},
 {'name':'AOL', 'shares': 20},
]

min_shares = min(s["shares"] for s in portfolio)
print(min_shares)