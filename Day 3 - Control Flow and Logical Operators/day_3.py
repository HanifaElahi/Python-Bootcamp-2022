###############################################################
# 29. Control Flow with if/else and Conditional Operators
###############################################################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")

else:
    print("Sorry, you have to grow taller before you can ride")

################################################################
# 31. Nested if statements and elif statements
###############################################################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride")

################################################################
# 34. Multiple if statements in Succession
################################################################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child tickets are $5.")

    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        #Add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride")

################################################################
# 36. Logical Operators
################################################################

a = 12

a > 15
# Ouput : False

a < 10
# Ouput : True

a > 10 and a < 13
# Ouput : True

a > 15 and a < 13
# Ouput : False

not a > 15
# Ouput : True

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child tickets are $5.")

    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        #Add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}.")
