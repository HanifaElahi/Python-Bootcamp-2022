###############################################################
# 50. Using Loop wih Python Lists
###############################################################

fruits = ["Stawberries", "Peach", "Apple", "Cherries", "Mango", "Pear"]

for fruit in fruits:
    #print(fruit)
    print(fruit + " Pie!")
print(fruits)

###############################################################
# 53. for Loop and the range() function
###############################################################

for number in range(1, 11):
    print(number)

total = 0

for number in range(1, 101):
    total += number

print(total)
