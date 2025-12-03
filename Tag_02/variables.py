from math import pi
# Day_2: 30 Days of Python programming

# Exercise 1

# 1
first_name = "Leon"
# 2
last_name = "Kühne"
# 3
full_name = "Leon Niclas Kühne"
# 4
country = "Deutschland (Germany)"
# 5
city = "Regensburg"
# 6
age = 21
# 7
year = 2025
# 7
is_married = False
# 8
is_true = True
# 9
is_light_on = False
# 10
first_name2, last_name2, age2, country2, city2, is_light_on2 = "Leon", "Kühne", 21, "Deutschland (Germany)", "Regensburg", False

# Exercise 2
# 1
print(type(first_name))
print(type(first_name2))
print(type(last_name))
print(type(last_name2))
print(type(full_name))
print(type(country))
print(type(country2))
print(type(city))
print(type(city2))
print(type(age))
print(type(age2))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(is_light_on2))
# 2
print(len(first_name))
# 3
print(f"Länge des Vornamen", len(first_name),"\nLänge des Nachnamen", len(last_name))
# 4
num_one = 5
num_two = 4
# 5
add = num_one + num_two
print(add)
# 6
sub = num_one - num_two
print(sub)
# 7
mult = num_one * num_two
print(mult)
# 8
div = num_one / num_two
print(div)
# 9
mod = num_one % num_two
print(mod)
# 10
exp = num_one ** num_two
print(exp)
# 11
fdiv = num_one // num_two
print(fdiv)
# 12
radius = float(input("Which radius the circle should have?"))
# i.
area_of_circle = pi * radius**2
print(f"The area of the circle is {area_of_circle:.2f} meters.")
# ii.
circum_of_circle = 2 * pi * radius
print(f"The circumference of the circle ist {circum_of_circle:.2f} meters.")
# iii.
# radius = input("Which radius the circle should have?")
# 13
first_name = input("What is your firstname?")
last_name = input("What is your lastname?")
country = input("Where you are from?")
age = input("How old are you?")
# 14
help("keywords")
