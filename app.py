#some functions of calculator
def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def devide(x,y):
    #y cannot be 0
    if y==0:
        return "ERROR, DEVIDE BY 0!/n Please try again"
    return x/y
