# Day_7: 30 Days of Python programming
a_set = {19, 22, 24, 20, 25, 26}
b_set = {19, 22, 20, 25, 26, 24, 28, 27}
# 1
c_set = a_set.union(b_set)
print(c_set)
# 2
print(a_set.intersection(b_set))
# 3
print(a_set.issubset(b_set))
# 4
print(a_set.isdisjoint(b_set))
# 5
d_set = a_set.union(b_set)
e_set = b_set.union(a_set)
print(d_set)
print(e_set)
# ===> d_set = e_set
# 6
sym_dif = a_set.symmetric_difference(b_set)
print(sym_dif)
# 7
del a_set
del b_set
try:
    print(a_set, b_set)
except NameError:
    print("set() not found.")
