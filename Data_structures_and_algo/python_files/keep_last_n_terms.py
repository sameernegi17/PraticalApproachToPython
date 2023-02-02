
"""
You want to keep a limited history of the last few items seen during iteration or during
some other kind of processing.
"""

from collections import deque

history = deque(maxlen=5)



with open("data/somefile.txt") as f:
    for line in f:
        history.append(line)
        print(history)
        print("------------------------------")
