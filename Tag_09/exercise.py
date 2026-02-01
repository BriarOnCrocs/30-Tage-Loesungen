# Day_9: 30 Days of Python programming
# 1
user = int(input("Enter your age please!: "))
if user >= 18:
    print("You are old enough to drive!")
else:
    missing_years = 18 - user
    print(f"You need {missing_years} more years to learn to drive.")
# 2
my_age = 21
your_age = int(input("Please enter your age!: "))
if my_age != your_age:
    difference = my_age - your_age
    if difference <= -2:
        years_older = difference
        print(f"You are {abs(difference)} years older than me!")
    elif difference >= 2:
        years_younger = difference
        print(f"You are {abs(difference)} years younger than me!")
    elif difference == -1:
        year_older = difference
        print(f"You are {abs(difference)} year older than me!")
    else:
        year_younger = difference
        print(f"You are {abs(difference)} year younger than me!")
else:
    print("We are the same age!")
# 3
a = int(input("Enter a Number (a) please!: "))
b = int(input("Enter a Number (b) please!: "))
if a > b:
    print(f"{a} is greater than {b}.")
elif b > a:
    print(f"{b} is greater than {a}.")
else:
    print(f"{a} is equal to {b}.")