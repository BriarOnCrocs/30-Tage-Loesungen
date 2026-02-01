# Day_11: 30 Days of Python programming
# 1
x = int(input("Enter x: "))
y = int(input("Enter y: "))

def add_two_numbers(fx, fy):
    sum_xy = x + y
    return sum_xy

print(f"The sum of {x} and {y} is", add_two_numbers(x, y))