"""
------------------------PYTHON FULL COURSE-----------------------------------
-----------------------------------------------------------------------------
"""


"""
------------------------DATA STRUCTURES (TUPLES)-----------------------------------
"""

##Tuples are like lists but they cant change their content

print("-----------------------DECLARING A LIST-----------------------")
##Empty list
t1 = ()
print(t1)
##list with 1 element
t2 = (15)
print(t2)
t3 = (True)
print(t3)

print("-----------------------ACCESSING LIST ITEMS-----------------------")
t4 = (1,5,32,True,"Hello",55,"Python",t3) ##t3 inside t4

##1st element
print(f"first elet = {t4[0]}")

##2nd element
print(f"second elet = {t4[1]}")

##last element
print(f"last elet = {t4[-1]}")

##before last element
print(f"before last elet = {t4[-2]}")

##series of elements (slicing)
print(f"elemnts from position 2 to position 5 = {t4[1:5]}") ##starts from index 1 to index 5


print("-----------------------GET LENGTH OF A LIST -----------------------")
print(len(t4))
print(len(t1))


print("-----------------------COUNT ELEMENT IN A LIST -----------------------")
total_55 = t4.count(55)
print(total_55)


print("-----------------------GET INDEX OF ELEMENT IN A LIST -----------------------")
t5 = [1,5,32,100]

try:
    item1 = t5.index(32)
    print(item1)
except ValueError: 
    print ("Value not existed in list")

try:
    item2 = t5.index(20)
    print(item2)
except ValueError: 
    print ("Value not existed in list")