"""
Unpacking a Sequence into Separate Variables
"""

p = (4,5)
print(p)
x,y = p
print("x ",x)
print("y ",y)

data = ["Acne",50,90.1,[2021,19,1]]
name,share,price,(year, day, month) = data
print("name ", name)
print("shares ", share)
print(f"{day}-{month}-{year}")

s = "hello"
a,b,c,d,e = "hello"

print(a,b,c,d)

data = ["Acne",50,90.1,[2021,19,1]]
name,share,_,(year, day, month) = data
print("name ", name)
print("shares ", share)
print(f"{day}-{month}-{year}")
