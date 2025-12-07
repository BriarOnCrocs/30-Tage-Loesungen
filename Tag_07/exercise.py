# Day_7: 30 Days of Python programming
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# 1
print(f"the length of the set() is {len(it_companies)}.")
# 2
it_companies.add("Twitter")
print(it_companies)
# 3
it_companies.update(["GitHub", "OpenAi", "SAP", "Siemens"])
print(it_companies)
# 4
it_companies.remove("IBM")
print(it_companies)
# 5
try:
    it_companies.discard("NotExisting")
    it_companies.remove("NotExisting")
except KeyError:
    print("Item not found")
# Other than .remove, .discard method does not raise any errors