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
# 20