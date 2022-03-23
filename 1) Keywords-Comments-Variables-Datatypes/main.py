"""
------------------------PYTHON FULL COURSE-----------------------------------
-----------------------------------------------------------------------------
"""


"""
------------------------KEYWORDS-COMMENTS-VARIABLES-DATATYPES-----------------------------------
"""


""" 
    (1) COMMENTS 
    *) they are not executed (just we write them to describe the code)
"""  

# 1 line comment

""" 
multy 
line 
comment
"""


""" 
    (2) KEYWORDS
    *) Keywords are the reserved words in Python
    *) We cannot use a keyword as a variable name, function name or any other identifier
    *) the are case sensitive

"""  

import keyword #called module (learn it later)
print("*********************(2) KEYWORDS ************************\n")#here print() is used to dispaly text ,\n to jump to new line 
print(keyword.kwlist) #here print is used to display results on screen, ... 
print("*********************************************************\n")


""" 
    3) DATA TYPES, VARIABLES, ....
    *) variable is a location stored in memory, 
    *) we give a variable a name (identifier) so we can access it
    *) in python we dont need to mention the type of the variable when we declare it
""" 

#None DATATYPE (means has no type yet)
nothing = None  #here we declared a variable named nothing and we assign to it the value None 


#integer DATATYPE (like 1  0  2   100   1456    ....)
i = 2 #here we declared a variable named i and we assign to it the value 2


#complex DATATYPE (like 1+2j  (1 is real part , 2 is the imaginary part))
cpx = 4 + 2j #here we declared a variable named cpx and we assign to it the value 4 + 2j


#float DATATYPE (like 11,3  20,3 ...)
f = 123456789.e3 #here we declared a variable named f and we assign to it the value 123456789 * 10^(3)


#boolean DATATYPE ( either True or False)
b = False #here we declared a variable named b and we assign to it the value False


#string DATATYPE (means text like "hello" 'hi' '''how are you''')
str1="hello" 
str2='hi'
str3="""welcome"""


print("*********************(3) DATATYPES-VARIABLES ************************\n")
print ("Type of (",nothing,")" ,"is ",type(nothing))
print ("Type of (",f,")" ,"is ",type(f))
print ("Type of (",i,")" ,"is ",type(i))
print ("Type of (",b,")" ,"is ",type(b))
print ("Type of (",cpx,")" , "is ", type(cpx))
print ("Type of (",str1,")" ,"is ",type(str1))
print ("Type of (",str2,")" ,"is ",type(str2))
print ("Type of (",str3,")" ,"is ",type(str3))
print("*********************************************************\n")