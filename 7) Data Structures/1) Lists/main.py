"""
------------------------PYTHON FULL COURSE-----------------------------------
-----------------------------------------------------------------------------
"""


"""
------------------------DATA STRUCTURES (LISTS)-----------------------------------
"""


##List can be seen as a collection: they can hold many variables. List resemble physical lists, they can contain a number of items.
##A list can have any number of elements. They are similar to arrays in other programming languages. Lists can hold all kinds of variables: integers (whole numbers), floats, characters, texts and many more.

print("-----------------------DECLARING A LIST-----------------------")
##Empty list
l1 = []
print(l1)
##list with 1 element
l2 = [15]
print(l2)
l3 = [True]
print(l3)

print("-----------------------ACCESSING LIST ITEMS-----------------------")
l4 = [1,5,32,True,"Hello",55,"Python",l3] ##l3 inside l4

##1st element
print(f"first elet = {l4[0]}")

##2nd element
print(f"second elet = {l4[1]}")

##last element
print(f"last elet = {l4[-1]}")

##before last element
print(f"before last elet = {l4[-2]}")

##series of elements (slicing)
print(f"elemnts from position 2 to position 5 = {l4[1:5]}") ##starts from index 1 to index 5


print("-----------------------GET LENGTH OF A LIST -----------------------")
print(len(l4))
print(len(l1))


print("-----------------------ADDING ELEMENTS TO A LIST -----------------------")

##add at the end
l4.append(100)
l4.append(l2)
print(l4)

##add at certain index
l4.insert(0,741) ##inserting 741 at the begining of the list l4
print(l4)


print("-----------------------DELETING ELEMENTS FROM A LIST -----------------------")

##delete the last element and return it 
last = l4.pop()
print(last)
print(l4)

##delete at certain index and return it
elt3 = l4.pop(2)
print(elt3)
print(l4)

##delete at certain index without returning the delted value
del l4[-2]
del l4[1]
print(l4)


##delete series of elements 
del l4[0:3]
print(l4)


##empty a list
l4.clear()
print(l4)

print("-----------------------GET INDEX OF ELEMENT IN A LIST -----------------------")
l5 = [1,5,32,100]

try:
    item1 = l5.index(32)
    print(item1)
except ValueError: 
    print ("Value not existed in list")

try:
    item2 = l5.index(20)
    print(item2)
except ValueError: 
    print ("Value not existed in list")

print("-----------------------COUNT ELEMENT IN A LIST -----------------------")
l5.append(5)
total_5 = l5.count(5)
total_10 = l5.count(10)
print(total_5)
print(total_10)


print("-----------------------COPY A LIST -----------------------")
print(l4)
l4 = l5.copy()
print(l5)

print("-----------------------REVERSE A LIST -----------------------")
print(l4)
l6 = l4.copy()
l6.reverse()
print(l6)


print("-----------------------SORT A LIST -----------------------")
l8 = l6.copy()
l9 = l6.copy()
l8.sort()
l9.sort(reverse=True)
print(l8)
print(l9)

print("-----------------------EXTEND A LIST -----------------------")
print(l1)
print(l9)
l1.extend(l9)
print(l1)

print(l2)
print(l8)
l2 = l2 + l8
print(l2)
