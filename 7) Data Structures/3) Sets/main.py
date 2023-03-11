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
random_elt = set1.pop() ##romoving an element randomly
print(random_elt)

print("-----------------------EMPTY A SET-----------------------")
print(set2)
set2.clear()
print(set2)

print("-----------------------COPY A SET-----------------------")
new_set = set1.copy()
print(new_set)

print("-----------------------UPDATE A SET BY DIFFERENT SETS-----------------------")
set1_cp = set1.copy()
set2_cp = set2.copy()
set3_cp = set3.copy()
elt = set1_cp.update(set2_cp,set3_cp,{15,32,1})
print(elt)
print(set1_cp)

print("-----------------------DIFFERENCE BETWEEN SETS-----------------------")
set1_cp = set1.copy()
set2_cp = set2.copy()
set3_cp = set3.copy()
uncommun_elt = set1_cp.difference(set2_cp,set3_cp,{15,32,1})
print(uncommun_elt)
print(set1_cp)

print("-----------------------DIFFERENCE BETWEEN SETS AND UPDATE-----------------------")
set1_cp = set1.copy()
set2_cp = set2.copy()
set3_cp = set3.copy()
set1_cp.difference_update(set2_cp,set3_cp,{15,32,1})
print(set1_cp)

print("-----------------------SYMETRIC DIFFERENCE BETWEEN SETS-----------------------")
set1_cp = set1.copy()
set2_cp = set2.copy()
set3_cp = set3.copy()
set1_cp.symmetric_difference(set3_cp)
print(set1_cp)

print("-----------------------SYMETRIC DIFFERENCE BETWEEN SETSAND UPDATE-----------------------")
set1_cp = set1.copy()
set2_cp = set2.copy()
set3_cp = set3.copy()
set1_cp.symmetric_difference_update(set2_cp)
print(set1_cp)

print("-----------------------INTERSECTION BETWEEN SETS-----------------------")
set1_cp = set1.copy()
set2_cp = set2.copy()
set3_cp = set3.copy()
commun_elt = set1_cp.intersection(set2_cp,set3_cp,{15,32,1})
print(commun_elt)
print(set1_cp)

print("-----------------------UNION BETWEEN SETS-----------------------")
set1_cp = set1.copy()
set2_cp = set2.copy()
set3_cp = set3.copy()
commun_elt = set1_cp.union(set2_cp,set3_cp,{15,32,1})
print(commun_elt)
print(set1_cp)


print("-----------------------SET IS DISJOINT WITH ANOTHER SET -----------------------")
set1_cp = set1.copy()
set2_cp = set2.copy()
set3_cp = set3.copy()
disjoint = set1_cp.isdisjoint({15,32,1})
print(disjoint)
print(set1_cp)

print("-----------------------SET I AN UPPER SET OF ANOTHER SET-----------------------")
set1_cp = set1.copy()
set2_cp = set2.copy()
set3_cp = set3.copy()
superset = set1_cp.issuperset({15,32,1})
print(superset)
print(set1_cp)


print("-----------------------SET I AN SUB SET OF ANOTHER SET-----------------------")
set1_cp = set1.copy()
set2_cp = set2.copy()
set3_cp = set3.copy()
subset = set1_cp.issubset({15,32,1})
print(subset)
print(set1_cp)
