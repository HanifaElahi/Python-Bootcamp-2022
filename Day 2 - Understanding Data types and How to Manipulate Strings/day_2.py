#####################################################
# 19. Python Primitive Data Types
#####################################################

print(len("Hello!"))
# Output : 6

print(len(123456))
# Output : Type Error: oject of type int has no len()

# String Subscripting
print("Hello!"[0])
# Output : H

print("123" + "456")
# Output : 123456

# Integer

print(123+456)
# Output : 579

print(123_456_789)
# Output : 123456789
#underscores could be added for clear visualization of large integers & thus ignored by computer

# Float

#3.14526

# Boolean

#True
#False

######################################################
#20. Type Error, Type Checking and Type Conversion
######################################################

#Type Error : can only concatenate str (not "int") to str
num_char = len(input("What is your name ? "))
print("your name has " + num_char + " characters.")
# Output : #Type Error : can only concatenate str (not "int) to str

new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")

print(type(num_char))
# Output : class <int>

a = 123
print(type(a))
# Output : <class 'int'>

a ="123"
print(type(a))
# Output : <class 'str'>

a = float(123)
print(type(a))
# Output : <class 'float'>

print(70 + float("100.32"))
# Output : 170.32 , first converted str to float and added 70

print(str(70) + str(100))
# Ouput: 70100

##############################################################
# 22. Mathematical Operations in Python
##############################################################

# Addition
print(3 + 5)
# Output : 8

# Subtraction
print(8 - 2)
# Output : 6

# Multiplication
print(4 * 7)
# Output : 28

# Division
print(50 / 5)
# Output : 10.0

#Whenever you divide we always end up with floating point number

# Exponent
print (2 ** 4)
# Output : 8

#PEMDASLR

#()
#**
#* /
#+ -
#Calculations goes from left to right

print(3 * 3 + 3 / 3 - 3)
# Output : 7.0

print(3 * (3 + 3) / 3 - 3)
# Output : 3.0

##############################################################
# 24. Number Manipulation and f-Strings in Python
##############################################################

print(8 / 3)
# Output : 2.666666666665

print(int(8 / 3))
# Output : 2

print(round(8/3))
# Output : 2

print((round(8 / 3), 3))
# Output : 3

print(round(2.66666666666666666667,2))
# Output : 2.67

# Floor Division
print(8 // 3)
# Output : 2

print(type(8/3))
# Output : <class 'float'>

print(type(8//3))
# Output : <class 'int'>

# Even if it's complete division, it would be still floating point number
print(type(4/2))
# Output : <class 'float'>

result = 4 / 2
result /= 2
print(result)
# Output : 1.0

score = 0
score += 1
print(score)
# Ouput : 1

score -= 1
print(score)
# Ouput : 0

# f-String
score = 0
height = 1.8
isWinning = True

print(
    f"Your score is {score}, your height is {height}, and your #are winning is {isWinning}"
)
