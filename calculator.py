# function
def menu():
    print("1) Sum")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")

# Call the function
menu()
# read the input of the keyboard
opt = input("Select the number of the Operation you'd like to perform")
# try to continue with the calculator app
firstNum = float(input("Please enter a number"))
secondNum = float(input("Please enter second number"))

if opt=="1":
    total = firstNum + secondNum
    print("The total is " + str(total) + ".")
elif opt == "2":
    total = firstNum - secondNum
    print("The total is " + str(total) + ".")
elif opt == "3":
    total = firstNum * secondNum
    print("The total is " + str(total) + ".")
elif opt == "4":
    if secondNum == 0:
        print("You cannot divide by 0.")
    else:
        total = firstNum / secondNum
        print("The total is " + str(total) + ".")
else:
    print("That's not a valid option.")



    