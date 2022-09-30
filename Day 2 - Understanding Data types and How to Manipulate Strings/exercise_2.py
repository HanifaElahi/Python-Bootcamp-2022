
###########################################################################################################################
#                                                    EXERCISE 2.2
###########################################################################################################################


# 🚨 Don't change the code below 👇
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#bmi = weight / height ** 2
#print(type(height), type(weight))

weight = int(weight)
height = float(height)

bmi = int(weight / height**2)
print(f"Your BMI is : {bmi}")