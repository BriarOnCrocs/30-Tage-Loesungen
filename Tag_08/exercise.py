# Day_8: 30 Days of Python programming
# 1
dog = {}
# 2
dog["name"], dog["color"], dog["breed"], dog["legs"], dog["age"] = "doggo", "brown", "Beagle", True , 15
print(dog)
# 3
student = {}
student["first_name"], student["last_name"], student["gender"], student["age"], student["martial_status"], student["skills"], student["country"], student["city"], student["address"] = "Leon", "Kühne", "male", 21, "engaged", ["Python", "Assembly", "HTML"], "Germany", "Regensburg", ("Rathausplatz 1")
print(student)
# 4
print(len(student))
# 5
value_skills = student.get("skills")
print(value_skills, type(value_skills))
# 6
