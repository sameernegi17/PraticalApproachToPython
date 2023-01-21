with open('data/file_tut.txt', 'r') as f:
    read_data = f.readline()
    print(read_data)
    print("*******************")
    read_data = f.readline()
    print(read_data)
    print("*******************")
    read_data = f.readline()
    print(read_data)



with open('data/file_tut.txt', 'r') as f:
    for line in f:
        print(line)

print("=========================")
with open('data/file_tut.txt', 'a') as f:
    f.write("\n 11 12 14 15 \n")

print("=========================")
with open('data/file_tut.txt', 'r') as f:
    f.readline()
    print(f.tell())

print("=========================")
f = open('data\workfile.txt', 'rb+')
print(f.seek(5))
print(f.read(1))
print(f.seek(-3,2))
print(f.read(1))
f.close()