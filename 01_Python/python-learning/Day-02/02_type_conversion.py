# Implicit Type Conversion

a = 10
b = 2.5
print(a + b)
print(type(a + b))
# python automatically converts data 
# python automaticaly converts 10(int) to 10.0(float).

# Explicit Type Conversion

num = "100"
print(int(num))
print(type(num))
print(type(int(num)))

# Common types conversion functions in Python

# int() - converts to integer
# float() - converts to floating-point
# str() - converts to string
# bool() - converts to boolean
# complex() - converts to complex number

# Examples
# String to Integer

x = "50"      # in string
print(int(x)) # converts to integer
print(type(x))
print(type(int(x)))

# Integer to Float 

x = 10      # in integer
print(float(x)) # converts to float
print(type(x))
print(type(float(x)))

# Float to Integer

x = 10.5      # in float
print(int(x)) # converts to integer
print(type(x))
print(type(int(x)))

# Integer to String 

X = 100     # in integer
print(str(X)) # converts to string
print(type(X))
print(type(str(X)))

# Integer to Boolean

print(bool(1)) # converts to boolean
print(bool(0)) # converts to boolean

# String to Boolean

print(bool("Hello")) # converts to boolean
print(bool(""))      # converts to boolean

# Practice

a = "25"
print(int(a)) # converts to integer
print(type(a))
print(type(int(a)))

b = 45 
print(str(b)) # converts to string
print(type(b))  
print(type(str(b)))

c = 12 
print(type(c))
print(float(c)) # converts to float
print(type(float(c)))

d = 9.8
print(type(d))
print(int(d)) # converts to integer
print(type(int(d)))

a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
print("Sum:", a + b)