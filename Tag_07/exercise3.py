# Day_7: 30 Days of Python programming
age = [22, 19, 24, 25, 26, 24, 25, 24]
# 1
set_age = set(age)
if len(age) > len(set_age):
    print(f"The length of {age} is bigger than {set_age}.")
else:
    print(f"The length of {set_age} is bigger than {age}.")
# 2
# The data type "str" can be contained in a list, set, tuple
# The data type "list" can store different values. A list can be modified (mutable), duplicates are allowed and can be sorted aswell.
# The data type "tuple" has the same properties as a list, but it is immutable.
# The data type "set" is mutable, unsorted and duplicates are not allowed.
# 3
sentence = "I am a teacher and I love to inspire and teach people"
split_sentence = sentence.split(" ")
tpl_sentence = set(split_sentence)
print(f"The unique word in: {sentence}\nare {tpl_sentence}")


# list – mutable, duplicates erlaubt, sortierbar
# tuple – wie list, aber immutable
# set – mutable, unsortiert, keine duplicates
# str – immutable, Text