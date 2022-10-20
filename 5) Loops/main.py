"""
------------------------PYTHON FULL COURSE-----------------------------------
-----------------------------------------------------------------------------
"""


"""
------------------------LOOPS-----------------------------------
"""

## FOR LOOP (used to itirate through a range, iterable objects)
## iterable objects are objects that contains multiple values (like arrays, lists , sets ,....etc)

## 

from time import sleep


print("------------------------FOR LOOP------------------------")

print("------------------------SIMPLE COUNTER USING FOR LOOP------------------------")

## range function set an intervale in this case : range(3) takes values 0,1,2
## range(n) takes values form 0 to n-1
## for loop iterate though the iterable object , in this case "range" 
## "range(3)" has 3 values 0,1,2 :so for loop will do 3 iteration
## for each iteration ,the loop will affect a value to "i", 
## first iteration "i" will take value 0
## second iteration "i" will take value 1
## third iteration "i" will take value 2
## after third iteration the code will exit the loop because if "i" will take value 3 then it wont be included in range(3), 3 is out of (range(3))
## sleep(1) allows the execution to freeze for 1s

for i in range(3):
    print(i+1)
    sleep(1)

print("let's Go !!!")