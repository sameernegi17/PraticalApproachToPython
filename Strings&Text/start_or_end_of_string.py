"""
Matching Text at the Start or End of a String

You need to check the start or end of a string for specific text patterns, such as filename
extensions, URL schemes, and so on.

"""

file = "spam.txt"
print(file.endswith("txt"))

url = "http://www.python.org"
print(url.endswith("org"))
print(url.startswith("http"))
print(url.startswith("https"))

import os

file = os.listdir(".")

pyfiles = [names for names in file if names.endswith("py")]

print(pyfiles)
