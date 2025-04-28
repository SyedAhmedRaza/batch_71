# Variables
message = "Hello, World!!!"
print(message)

# Data types
# 1) String
name = "Ahmed raza"
# 2) Integer
age = 28
# 3) Boolean
isMarried = False


# Variable with same name
name = "Raza"
name = "Hassan"
print(name)


# Concatenation
firstName = "Ahmed"
lastName = "Raza"
fullName = firstName + " " + lastName
print(fullName)


# f-strings
firstName = "Ahmed"
lastName = "Raza"
fullName = f"Hello {firstName} {lastName}"
print(fullName)


_name = "Ahmed"
name = "Ahmed Raza"
age = 28
print(f"Hello {name}, you are {age} years old.")


name = "Ahmed Raza"
print(type(name))
print(id(name))


# Operators
# Arithmetic Operators
# Comparison Operators
# Logical Operators
# Assignment Operators


# Arithmetic Operators
# + - * / % // **
# c = a - b
# c = a * b
# c = a / b
# c = a % b
# c = a // b
# c = a ** b # 10^3 = 10*10*10
a = 10
b = 3
print(10 + b - 2 * a + 10)
#     10 + 3    -20  + 10
#     10 + 3        -10
#        3

# Comparison Operators
# == != > < >= <=
a = 10
b = 10
c = a == b
c = a != b
c = a > b
c = a < b
c = a >= b
c = a <= b
print(c)