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