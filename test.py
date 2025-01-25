print ("Hello, World!")

#variables
name = "Derrick"
last_name = "Lapp"
age = 31
found = False
print (name, last_name)

#if / statment
if age < 100:
    print ("No worries, you're not that old!")
    print ("I'm using the indentation")
    print ("I'm out of the if statement")
elif age == 100: #elif=else if
    print ("Wow! You're a century old!")
else:
    print ("It seems you're really old!")


# Functions
def say_hello():
    print("Hello, World!")

def say_goodbye(name):
    print ("Goodbye, " + str(name)) #Need to convert to string if you want to concatenate string and a number

# Call functions
say_hello()
say_goodbye(2)


# Arrays are called lists
color = ["red", "green", "blue", "yellow"]
print (color)
# add an elemnent
color.append ("pink")
print (color)
print (color[0])
color.remove("blue")
print (color)

# for loop
for col in color:
    print (col)

# dictionaries
me = {
    "name": "Derrick",
    "last_name": "Lapp",
    "age":31
}
print (me["last_name"])
me["last_name"] = "NewLapp"
print(me)
me["color"] = "Yellow"
print(me)


ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]

# print the sum of all the numbers
def ex1():
    total = 0
    for age in ages:
        total = total + age
    print(total)
# Count how many users are equal or older than 21
# My version
def ex2():
    for adults in ages:
        if adults >= 21:
            adults += 1
    print(adults)
# Adrian's version
def Adex2():
    counter = 0
    for age in ages:
        if age >= 21:
            counter += 1
    print(counter)
# How many users are between 30 and 40 years old
# My Version
def ex3():
    counter = 0
    for age in ages:
        if age >= 30:
            if age <= 40:
                counter += 1
            else:
                counter += 0
        else:
            counter += 0
    print(counter)
# Adrian Version
def Adex3():
    counter = 0
    for age in ages:
        if age >= 30 and age <= 40:
            counter += 1
    print("There are " + str(counter) + " users between 30 and 40.")

# Call the functions
ex1()
ex2()
Adex2()
ex3()
Adex3()