###############################################################
# 41. Random Module
###############################################################

import random
import my_module

random_int = random.randint(1, 10)
print(random_int)
# Output : 7

random_float = random.random()
print(random_float)
# Output : 0.66998485950735355
# Generate between 0 and 1

love_score = random.randint(0, 100)
print(f"Your love score is {love_score}")
# Output : Your love score is 74

#print(my_module.pi)
# Output : 3.1519

###############################################################
# 43. Understanding the Offset and appending items to List
###############################################################

states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#print(states_of_america[0])
# Output : Dalaware

#print(states_of_america[-1])
# Output : Hawaii

#states_of_america[1] = "Pencilvania"
#print(states_of_america[1])
# Output : Pencilvania

#states_of_america.append("Wonderland")  #Will append at end
#print(states_of_america)

#states_of_america.extend(["Wonderland", "Funland"]) # Can append list
#print(states_of_america)

###############################################################
# 45. Index Errors and working with Nested Lists
###############################################################

#print(len(states_of_america))
# Output : 50

num_of_states = len(states_of_america)
#print(states_of_america[num_of_states])
# Output : IndexError: list index out of range

print(states_of_america[num_of_states - 1])
# Output : Hawii

fruits = [
    "Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
    "Peaches"
]

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
