name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "!" " You're " + age)

# 08/30/2023 tuples

coordinates = (4,5)
# tuples are immutable - coordinates[1] = 10 doesn't work
print(coordinates[0])

# list is mutable so the second line can change the list

test_list = [1,2,3,4,5]
test_list[1] = 10
print(test_list)

# making a function by typing def
def say_hi():
    print("Hello")

print("top")
say_hi()
print("bottom")

def say_hey(name):
    print("Hey! " + name)

say_hey("Mike")
say_hey("Jack")

def calculator_3_multiplies(number):
    print(3*number)

calculator_3_multiplies(3)

# return function
# return allows python to give back to the number
def cube(number):
    return number*number*number

# using result, you can print out result
print(cube(4))

def cube_3(num):
    return num*num*num

result = cube_3(2)
print(result)

# For Loops
# Function keeps showing until it hits the last of it 
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

# now the function keeps showing the list until x == "banana"
# printing the results before exiting the loop
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# print after exiting the loop
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        break
print(x)