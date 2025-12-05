from math import pi, sqrt
# Day_3: 30 Days of Python programming
# 1
age = 21
# 2
height = 184.0
# 3
complex_number = 1 + 6j
# 4
base_triangle = float(input("Please enter the base of the triangle!: "))
height_triangle = float(input("Please enter the height of the triangle!: "))

area_of_triangle = 0.5 * base_triangle * height_triangle

print(f"The area of your triangle is {area_of_triangle:.2f} cm^2!")
# 5
side_a = float(input("Please enter side a to calculate the perimeter of your triangle! "))
side_b = float(input("Please enter side b to calculate the perimeter of your triangle! "))
side_c = float(input("Please enter side c to calculate the perimeter of your triangle! "))

perimeter_of_triangle = side_a + side_b + side_c

print(f"The perimeter of your triangle is {perimeter_of_triangle:.2f} cm!")
# 6
length_of_rectangle = float(input("Please enter the length of your rectangle! "))
width_of_rectangle = float(input("Please enter the width of your rectangle! "))

area_of_rectangle = length_of_rectangle * width_of_rectangle
circumference_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)

print(f"The area of your rectangle is {area_of_rectangle:.2f}cm^2 and \nthe cirumference of your rectangle is {circumference_of_rectangle:.2f}cm! ")
# 7
radius_of_circle = float(input("Please enter the radius of your circle! " ))

area_of_circle = pi * radius_of_circle**2
circumference_of_circle = 2 * pi * radius_of_circle

print(f"The area of your circle is {area_of_circle:.2f}cm^2 and \nthe circumference of your circle is {circumference_of_circle:.2f}cm!")
# 8
y1_8 = 0
x1_8 = 1
y2_8 = 2
x2_8 = 2

slope_m8 = (y2_8-y1_8)/(x2_8-x1_8)
y_intercept8 = (0, -2)
x_intercept8 = (1, 0)

print(f"The slope of y = 2x -2 is: {slope_m8}.")
print(f"The y-intercept and x-intercept of y = 2x -2 are: {y_intercept8} and: {x_intercept8}.")
# 9
y1_9 = 2
x1_9 = 2
y2_9 = 10
x2_9 = 6

slope_m9 = (y2_9-y1_9)/(x2_9-x1_9)
print(f"The slope of point (2, 2) and point (6,10) is: {slope_m9}.")
ec_distance = sqrt((x1_9 - x2_9)**2 + (y1_9 - y2_9)**2)
print(f"The Euclidean distance between point (2, 2) and point (6,10) is {ec_distance:.2f}cm.")
# 10
print(slope_m8 == slope_m9)
# 11 y is 0 when x is -3
x_value = float(input("Please enter a value for the term x: "))
y_value = x_value**2 + 6*x_value + 9
print(f"The value of y is {y_value:.2f}.")
# 12
list_1 = ["python", "dragon"]
print(f"The length of python is {len(list_1[0])} and the lenth of dragon is {len(list_1[1])}")
print(len(list_1[0]) != len(list_1[1]))
# 13
print("on" in list_1[0] and "on" in list_1[1])
# 14
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)
# 15
print("on" not in list_1[0] and "on" not in list_1[1])
# 16
length_python = float(len(list_1[0]))
str_python = str(length_python)
print(f"The type of {str_python} is {type(str_python)}.")
# 17
input_number = int(input("Enter a number to check if it is even or not "))
check_number = input_number % 2
if check_number == 0:
    print(f"The number {input_number} is even!")
else:
    print(f"The number {input_number} is not even!")
# 18
floor_div = 7 // 3
int_number = int(2.7)
print(floor_div == int_number)
# 19
print(type("10") == type(10))
# 20
print(int(float("9.8")) == 10)
# 21
enter_hours = float(input("Enter hours: "))
enter_rate_per_hour = float(input("Enter rate per hour: "))
earning = enter_hours * enter_rate_per_hour
print(f"Your weekly earning is {earning:.2f}!")
# 22
years = float(input("Enter number of years you have lived: "))
years_in_seconds = (((years * 365) * 24) * 3600)
print(f"You have lived for {years_in_seconds:.2f} seconds.")
# 23
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)