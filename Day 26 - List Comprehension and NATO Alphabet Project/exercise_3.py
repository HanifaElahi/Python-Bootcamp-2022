
###########################################################################################################################
#                                                    EXERCISE 26.3
###########################################################################################################################

with open('file1.txt') as file:
    file_1_data = file.readlines()

with open('file2.txt') as file:
    file_2_data = file.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

# Write your code above 👆

print(result)