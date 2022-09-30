
###########################################################################################################################
#                                                    EXERCISE 2.1
###########################################################################################################################

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
#print(type(first_digit, second_digit))

result = int(first_digit) + int(second_digit)
print(f"Its Sum is : {result}")