"""
You have two dictionaries and want to find out what they might have in common (same
keys, same values, etc.).
"""

a = {"x": 1, "y": 2, "z": 3}

b = {"w": 10, "x": 11, "y": 2}

print(a.keys() | b.keys()) #union

#intersection
print(a.keys() & b.keys()) 

#difffernce
print("Differnce")
print(a.keys() - b.keys()) 
print(b.keys() - a.keys()) 