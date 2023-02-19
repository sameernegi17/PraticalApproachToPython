"""
Removing Duplicates from a Sequence while
Maintaining Order

You want to eliminate the duplicate values in a sequence, but preserve the order of the
remaining items.
"""
def dedupe(items):
   seen = set()
   for item in items: 
       if item not in seen:
            yield item
       seen.add(item) 


a = [1,5,2,1,9,1,5,10]

print(list(dedupe(a)))

