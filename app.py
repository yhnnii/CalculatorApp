import math
#some functions of calculator

#option 1
def add(x,y):
    return x+y

# option 2
def substract(x,y):
    return x-y

# option 3
def multiply(x,y):
    return x*y

#option 4
def devide(x,y):
    #y cannot be 0
    if y==0:
        return "ERROR, DEVIDE BY 0!/n Please try again"
    return x/y

# option 5
def power(x,y):
    return x**y

#option 6
def sqrtroot(x):
    return math.sqrt(x)


# operation part
print("operation selections: ")
print("1, add")
print("2, substract")
print("3, multiply")
print("4, divide")
print("5, power")
print("6, square root")
