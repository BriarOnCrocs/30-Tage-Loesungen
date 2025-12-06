# Day_4: 30 Days of Python programming
# 1

first_str = "Thirty "
second_str = "Days "
third_str = "Of "
fourth_str = "Python"
full_str = first_str + second_str + third_str + fourth_str
print(full_str)
# 2
first_str2 = "Coding "
second_str2 = "For "
third_str2 = "All"
full_str2 = first_str2 + second_str2 + third_str2
print(full_str2)
# 3
company = "Coding For All"
# 4
print(company)
# 5
print(len(company))
# 6
print(company.upper())
# 7
print(company.lower())
# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())
# 9
print(company[:6:1])
# 10
found = company.find("Coding")
print(f"The word \"Coding\" has the index {found}.")
found_2 = company.index("Coding")
print(f"The word \"Coding\" has the index {found_2}.")
found_3 = company.rindex("Coding")
print(f"The word \"Coding\" has the index {found_3}.")
# 11
replaced = company.replace("Coding", "Python")
print(replaced)
# 12
normal = "Python for Everyone"
replaced_2 = normal.replace("Everyone", "All")
print(f"\"{normal}\" was replaced with \"{replaced_2}\".")
print(f"\"{normal}\" was replaced with \"{normal.strip("Everyone") + "All"}\"")
# 13
listed = company.split(" ")
print(listed)
# 14
split_str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
comma_split = split_str.split(", ")
print(comma_split)
# 15
print(f"Character of \"Coding For All\" at index 0: {company[0]}")
# 16
print(f"Character of \"Coding For All\" at index -1: {company[-1]}")
# 17
print(f"Character of \"Coding For All\" at index 10: {company[10]}")
# 18
split_normal = normal.split(" ")
for word in split_normal:
    print(word[0].upper(), end="")
# 19
print("")
split_company = company.split(" ")
for word in split_company:
    print(word[0].upper(), end="")
print("")
# 20
print(company.index("C"))
# 21
print(company.index("F"))
# 22
print(company.rfind("l"))
# 23
bc_sentence = "You cannot end a sentence with because because because is a conjunction"
print(bc_sentence.index("because"))
print(bc_sentence.find("because"))
# 24
print(bc_sentence.rfind("because"))
# 25
only_bc = bc_sentence[31:54]
print(only_bc)
# 26
print(bc_sentence.index("because") + 1)
# 27
print(only_bc)
# 28
print(company.startswith("Coding"))
# 29
print(company.endswith("Coding"))
# 30
given_string = "   Coding For All      "
print(given_string.strip(" "))
# 31
identify_1 = "30DaysOfPython"
identify_2 = "thirty_days_of_python"
print(f"Is the string: {identify_1} a valid variable name --> {identify_1.isidentifier()}")
print(f"Is the string: {identify_2} a valid variable name --> {identify_2.isidentifier()}")
# 32
libaries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
hash_libaries = " # ".join(libaries)
print(hash_libaries)
# 33
print("I\nam\nenjoying\nthis\nchallenge.\n")
print("I\njust\nwonder\nwhat\nis\nnext.\n")
# 34
print("Name\t\tAge\t\tCountry\t\tCity")
print("Asabeneh\t250\t\tFinland\t\tHelsinki")
# 35
radius = 10
area = 3.14 * radius ** 2
string_35 = "The area of a circle with radius {} is {:.2f} meters square.".format(radius, area)
print(string_35)
# 36
number1 = 8
number2 = 6
print("{} + {} = {}".format(number1, number2, number1  + number2))
print("{} - {} = {}".format(number1, number2, number1  - number2))
print("{} * {} = {}".format(number1, number2, number1  * number2))
print("{} / {} = {:.2f}".format(number1, number2, number1  / number2))
print("{} % {} = {}".format(number1, number2, number1  % number2))
print("{} // {} = {}".format(number1, number2, number1  // number2))
print("{} ** {} = {}".format(number1, number2, number1  ** number2))