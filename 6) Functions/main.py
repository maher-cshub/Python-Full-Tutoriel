"""
------------------------PYTHON FULL COURSE-----------------------------------
-----------------------------------------------------------------------------
"""


"""
------------------------FUNCTIONS-----------------------------------
"""

## A FUNCTION is a piece of code that runs each time we call (invoke) it
##A FUNTION can have input (argument like an integer , a float ,..etc) and can return a value or multiple values


print("------------------------DECLARING A FUNCTION------------------------")
##declaring a function (means defining a function "not execution")

##this function named "sum" 
##this functions takes 2 inputs (a and b)
##this function calculate the sum (a+b) and store it in variable c
##this function returns the variable c 

def sum(a,b): 
    c = a + b
    return c

def say_hello():
    print("Hello There")

print("------------------------CALLING (INVOKING) A FUNCTION------------------------")
##caling a FUNCTION Means execute it

##we called (invoked) the function sum so it will be executed ,and we passsed the 2 arguments (first = 5, second = 2), returned value will be stored in the variable returned_value
returned_value = sum(5,2) 
print(returned_value)
say_hello()

##we can specify our argument when we call a function
def say_name(firstname,lastname):
    print(f"Hello {firstname} {lastname}")

say_name(lastname="Jobs",firstname="Steve")
##if not you would see this
say_name("Jobs","Steves")

##after the first return statement all code below it wont be executed
def first_love(a,b):
    return f"{a} is my first love"
    return f"{b} is my second love"

love = first_love("Computer","Science")
print(love)

print("------------------------PASSING MULTIPLE ARGUMENT TO A  FUNCTION------------------------")
## if we dont know how much inputs we should pass to a function we can use (*var_name) as an argument (it will store a tuple of arguments)

def total_sum(*vars):
    sum = 0
    for var in vars:
        sum += var
    return sum
sum = total_sum(12,51,21,56,562,23,56,2398,35358,12480)
print(f"Total Sum = {sum}")
sum = total_sum(12)
print(f"Total Sum = {sum}")
sum = total_sum()
print(f"Total Sum = {sum}")

print("------------------------RETURNING MULTIPLE VALUES FROM A FUNCTION------------------------")
##to return multiple values from a function we separate them with a comma (,)

def show_full_name(firstname,lastname):
    return firstname,lastname

x,y = show_full_name("Steve","Jobs")
print(f"your full name is {x} {y}")


print("------------------------ANONYMOUS FUNCTION------------------------")
##ANONYMOUS FUNCTION (called lambda) is a function without a name
##this lambda function takes 2 arguments (x,y) execution starts after (:) it calcultes the sum of (a,b) ,returned value stored at sum2
sum2 = lambda x,y: x+y

print(f"sum of (5+10) = {sum2(5,10)}")


print("------------------------ARGUMENTS SCOPE------------------------")
##variable declared inside a function are called (local varible) ,can be accessed inside the function only
##variable declared outside a function (in the main program) are called (global varible) ,can be accessed inside the function and outside the function

total = 0

def total_func(x,y):
    total = x + y
    print(f"Inside the function total = {total}")


total_func(100,50)
print(f"Outside the function total = {total}")



