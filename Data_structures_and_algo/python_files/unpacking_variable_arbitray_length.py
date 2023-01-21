"""
Unpacking Elements from Iterables of Arbitrary Length
"""

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email,*phone_numbers  = record
print(name,  email, *phone_numbers)

records = [ ('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4), ] 

def foo_do(x,y):
    print(x,y)

def  bar_do(x):
    print(x)

for tag, *args in records:
    if tag == "foo":
        foo_do(*args)
    if tag == "bar":
        bar_do(*args)

record = ('ACME', 50, 123.45, (12, 18, 2012)) 
name, price ,*_ = record
print(name)

items = [7,10,15,6,9]
head,*tails = items
print(head,tails)

def sum(items):
    head,*tail = items
    return head + sum(tail) if tail else head

print(sum([7,10,15,6,9]))