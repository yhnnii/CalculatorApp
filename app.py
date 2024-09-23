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
def divide(x,y):
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

#execution

while True:
    print("Hello, welcome!")
    choice=input("Please Enter Operation Choice: ")

    if choice == "6":
        try: 
            num=float(input("Please enter number that you wish to do the square root: "))
        except ValueError:
            print("Invalid Input, enter number only")
            continue
        
        print(f"square root of {num} = {sqrtroot(num)}")
    
    elif choice in ["1","2","3","4","5"]:
        try:
            num1 = float(input("Please enter first number: "))
            num2 = float(input("Please enter second number: "))
        except ValueError:
            print("Invalid input, enter number only")
            continue

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {substract(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == "5":
            print(f"{num1} to the power of {num2} = {power(num1, num2)}")
    else:
        print("Invalid choice, please choose among 1,2,3,4,5,6")
    

    ans=input("Do you want to do another calculation? (Y/N): ")
    print(ans)
    if ans=="N" or ans=="n": 
        print("Thanks for using the calculator!")
        print("Have a good day!")
        break
    elif ans=="Y" or ans=="y":
        print("let's do another calculation")
        continue
    else:
        print("I don't understand, but I assume you want to do another calculation")
        print("so let's do another one,haha")
        continue
