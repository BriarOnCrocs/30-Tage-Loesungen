# Day_10: 30 Days of Python programming
# 1
count = 0
for e in range(1, 101):
    count = count + e
print(f"Sum: {count}")
# 2
even_num = 0
odd_num = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_num += i
    else:
        odd_num += i
print(f"Even numbers: {even_num}\nOdd numbers: {odd_num}")
