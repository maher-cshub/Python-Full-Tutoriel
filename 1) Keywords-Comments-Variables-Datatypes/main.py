"""
------------------------PYTHON FULL COURSE-----------------------------------
-----------------------------------------------------------------------------
"""



""" 1) comments """  

# 1 line comment

""" 
multy 
line 
comment
"""


""" 2) python keywords """  
import keyword
print(keyword.kwlist)



""" 3) data types, variables, .... """ 
#none
nothing = None

#float 
f = 123456789.e3

#integer
i = 2

#boolean
b = False

#string
str1="hello"
str2='hi'
str3="""welcome"""

#complex
cpx = 4 + 2j

print ("(",nothing,")" ,"of type ",type(nothing))
print ("(",f,")" ,"of type ",type(f))
print ("(",i,")" ,"of type ",type(i))
print ("(",b,")" ,"of type ",type(b))
print ("(",str1,")" ,"of type ",type(str1))
print ("(",str2,")" ,"of type ",type(str2))
print ("(",str3,")" ,"of type ",type(str3))
