
###########################################################################################################################
#                                                    EXERCISE 26.4
###########################################################################################################################

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
# print(sentence.split())

result = {word:len(word) for word in sentence.split()}

print(result)