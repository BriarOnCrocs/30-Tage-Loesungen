# Day_6: 30 Days of Python programming
# 1

tpl_members = tuple()
# 2
tpl_members = ("Briar", "Qiyana", "Viego", "Poppy", "Pantheon", "Milio", "Samira")
print(tpl_members)
# 3
brothers = ("Viego", "Pantheon", "Milio")
sisters = ("Briar", "Qiyana", "Poppy", "Samira")
siblings = brothers + sisters
print(siblings)
# 4
print(f"I have {len(siblings)} siblings.")
# 5
family_members = siblings + ("Aatrox", "Diana")
print(siblings)
print(family_members)