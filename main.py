fav_foods = []

# while loops:
# 1. run WHILE the condition is ture

user_food = input("Gimme 1 of your fav foods. Enter 'done' when you are finished: ")

#done is the "kill phrase"
while user_food != 'done':
  # append new items to fav_foods
  # ask the user for another entry
  fav_foods.append(user_food)
  user_food = input("Gimme 1 of your fav foods. Enter 'done' when you are finished: ")
''''''

print(fav_foods)