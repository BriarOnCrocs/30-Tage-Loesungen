# Day_9: 30 Days of Python programming
# 1
score = int(input("Please enter your score: "))

def grades(fscore):
    if 90 <= fscore <= 100:
        return "A"
    elif 80 <= fscore <= 89:
        return "B"
    elif 70 <= fscore <= 79:
        return "C"
    elif 60 <= fscore <= 69:
        return "D"
    else:
        return "F"

grade = grades(score)

print(f"The grade for the score {score} ist {grade}")
# 2
month = str(input("Enter a month to see the season: ")).lower()

def seasons(fmonth):
    if fmonth in ("september", "october", "november"):
        return "Autumn"
    elif fmonth in ("december", "january", "february"):
        return "Winter"
    elif fmonth in ("march", "april", "may"):
        return "Spring"
    elif fmonth in ("june", "july", "august"):
        return "Summer"
    else:
        return f"error, no valid month"

season = seasons(month)

print(f"The season for \"{month.capitalize()}\" is {season}.")
# 3
new_fruit = str(input("Enter a new fruit!: "))
fruits_list = ['banana', 'orange', 'mango', 'lemon']
def fruits(fnew_fruit):
    if fnew_fruit not in fruits_list:
        fruits_list.append(fnew_fruit)
        return fruits_list
    else:
        return f"{fnew_fruit.capitalize()} is already in the list: {fruits_list}"

add_to_list = fruits(new_fruit)
print(f"New list: {add_to_list}.")
