# Day_9: 30 Days of Python programming
# 1
score = int(input("Please enter your score: "))

def grades(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

grade = grades(score)

print(f"The grade for the score {score} ist {grade}")
# 2
month = str(input("Enter a month to see the season: ")).lower()

def seasons(month):
    if month in ("september", "october", "november"):
        return "Autumn"
    elif month in ("december", "january", "february"):
        return "Winter"
    elif month in ("march", "april", "may"):
        return "Spring"
    elif month in ("june", "july", "august"):
        return "Summer"
    else:
        return f"error, no valid month"

season = seasons(month)

print(f"The season for \"{month.capitalize()}\" is {season}.")
# 3
new_fruit = str(input("Enter a new fruit!: "))
fruits_list = ['banana', 'orange', 'mango', 'lemon']
def fruits(new_fruit):
    if new_fruit not in fruits_list:
        fruits_list.append(new_fruit)
        return fruits_list
    else:
        return f"{new_fruit.capitalize()} is already in the list: {fruits_list}"

add_to_list = fruits(new_fruit)
print(f"New list: {add_to_list}.")
