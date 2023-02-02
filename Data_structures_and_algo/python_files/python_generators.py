def firstn(n):
    num = 0
    while num < n:
        print("Before Return")
        yield num
        print("After Return")
        num += 1


print(sum(firstn(10000000)))