# Day_10: 30 Days of Python programming
# 1
for x in range(11):
    print(x)

count = 0
while count < 11:
    print(count)
    count = count + 1
# 2
for i in range(10, -1, -1):
    print(i)

count = 10
while count >= 0:
    print(count)
    count = count - 1
# 3
for e in range(1, 8):
    print("#"*e)

count = 1
while count <=7:
    print("#"*count)
    count = count + 1
# 4
for e in range(8):
    for i in range(8):
        print("#", end=" ")
    print("")
# 5
count = 0

while count <= 10:
    solution = count*count
    print(f"{count} x {count} = {solution}")
    count = count + 1
# 6
lst = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for e in lst:
    print(e, end=" ")
print(" ")
# 7
for e in range(101):
    if e % 2 == 0:
        print(e, end=" ")
    else:
        continue
print(" ")
# 8
for e in range(101):
    if e % 2 != 0:
        print(e, end=" ")
    else:
        continue
print(" ")