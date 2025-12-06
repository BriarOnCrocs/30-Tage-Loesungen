# Day_5: 30 Days of Python programming
# 1

lst = list() # or lst = []
# 2
liste = ["Briar", "Qiyana", "Viego", "Poppy", "Pantheon", "Milio", "Samira"]
# 3
print(len(liste))
# 4
print(liste[0], liste[3], liste[6])
# 5
mixed_data_types = ["Leon", 21, "184 cm", "engaged", "Regensburg"]
# 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# 7
print(it_companies)
# 8
print(f"Number of companies in this list: {len(it_companies)}")
# 9
print(it_companies[0], it_companies[3], it_companies[6])
# 10
it_companies.remove("Apple")
print(it_companies)
# 11
it_companies.append("Nvidia")
print(it_companies)
# 12
it_companies.insert(5, "AMD")
print(it_companies)
# 13
idx = it_companies.index("Amazon")
it_companies[idx] = it_companies[idx].upper()
print(it_companies)
# 14
joined_hash = " # ".join(it_companies)
print(joined_hash)
# 15
user = input("Enter an IT_Company!: ").lower()
lower_it_companies = [copy.lower() for copy in it_companies]

"""lower_it_companies = []
for copy in it_companies:
    lower_it_companies.append(copy.lower())"""

if user in lower_it_companies:
    print(f"Yes, {user.capitalize()} is in the list!")
else:
    print(f"No, {user.capitalize()} is not in the list!")
# 16
it_companies.sort()
print(it_companies)
# 17
"""
it_companies.sort(reverse=True)
"""
it_companies.sort()
it_companies.reverse()
print(it_companies)
# 18
first_three = it_companies[0:3]
print(first_three)
# 19
last_three = it_companies[-3:]
print(last_three)
# 20
middle_companies = len(it_companies) // 2
middle = it_companies[middle_companies]
print(middle)
# 21
it_companies.pop(0)
print(it_companies)
# 22
del it_companies[3:5]
print(it_companies)
# 23
it_companies.pop()
print(it_companies)
# 24
it_companies.clear()
print(it_companies)
# 25
del it_companies
try:
    print(it_companies)
except NameError:
    print("!it_companies was deleted!")
# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
# 27
full_stack = front_end.copy()
full_stack.insert(5, "Python")
full_stack.insert(5, "SQL")
print(full_stack)