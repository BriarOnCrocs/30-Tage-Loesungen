# Day_6: 30 Days of Python programming

family = ('Viego', 'Pantheon', 'Milio', 'Briar', 'Qiyana', 'Poppy', 'Samira', 'Aatrox', 'Diana')
print(family)
# 1
siblings = family[:7]
print(siblings)
parents = family[-2:]
print(parents)
# 2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ("milk", "egg", "honey", "fish")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# 3
food_stuff_lt = list(food_stuff_tp)
# 4
if len(food_stuff_lt) % 2 == 0:
    upper = len(food_stuff_lt) // 2
    lower = (len(food_stuff_lt) // 2) - 1
    middle_slice = food_stuff_lt[lower: upper + 1]
    print(f"2 items were sliced out: {middle_slice}")
else:
    middle = len(food_stuff_lt) // 2
    middle_slice = food_stuff_lt[middle: middle +1 ]
    print(f"1 items were sliced out: {middle_slice}")
# 5
first_three = food_stuff_lt[:3]
print(first_three)
last_three = food_stuff_lt[-3:]
print(last_three)
# 6
del food_stuff_tp
try:
    print(food_stuff_tp)
except NameError:
    print(f"There is no obj called food_stuff_tp.")
# 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)