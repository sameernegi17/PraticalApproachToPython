"""
Grouping Records Together Based on a Field

You have a sequence of dictionaries or instances and you want to iterate over the data
in groups based on the value of a particular field, such as date.

"""

from operator import itemgetter
from itertools import groupby



rows = [
    {"address": "5412 N CLARK", "date": "07/01/2012"},
    {"address": "5148 N CLARK", "date": "07/04/2012"},
    {"address": "5800 E 58TH", "date": "07/02/2012"},
    {"address": "2122 N CLARK", "date": "07/03/2012"},
    {"address": "5645 N RAVENSWOOD", "date": "07/02/2012"},
    {"address": "1060 W ADDISON", "date": "07/02/2012"},
    {"address": "4801 N BROADWAY", "date": "07/01/2012"},
    {"address": "1039 W GRANVILLE", "date": "07/04/2012"},
]

rows.sort(key=itemgetter("date"))

for date,items in groupby(rows,key=itemgetter("date")):
    print(date)
    for i in items:
        print(" ", i)

from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
   rows_by_date[row['date']].append(row)


print(rows_by_date)