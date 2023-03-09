"""
------------------------PYTHON FULL COURSE-----------------------------------
-----------------------------------------------------------------------------
"""


"""
------------------------DATA STRUCTURES (SETS)-----------------------------------
"""

##A SET is an unordered collection of immutable data ,with no duplicate items

print("-----------------------DECLARING A SET-----------------------")
##Empty set
set1 = set()
print(set1)
##set with 1 element
set2 = {15}
print(set2)
set3 = {True}
print(set3)

print("-----------------------GET LENGTH OF A SET -----------------------")
print(len(set1))
print(len(set3))

print("-----------------------ADDING ELEMENTS TO A SET -----------------------")
set1.add(15)
print(set1)

print("-----------------------REMOVING ELEMENTS FROM A SET WITHOUT RETURNING-----------------------")
set1.add(True)
set1.add(False)
set1.add(100)
set1.add(1.2)
print(set1)
set1.discard(False) ##doesnt rise an error if value not found
print(set1)
try:
    set1.remove(123) ##rises a KeyError if value not found
except KeyError:
    print("Value not found")

print("-----------------------EMPTY A SET-----------------------")
print(set2)
set2.clear()
print(set2)


