"""
------------------------PYTHON FULL COURSE-----------------------------------
-----------------------------------------------------------------------------
"""


"""
------------------------OPPERATORS-----------------------------------
"""



a= 11
b = 3
c = 0b11001100
d = 0b10011001
##arithmetic opperators 
## + (Addition)
print('a + b =',a+b)
## - (substraction)
print('a - b =',a-b)
## * (multiplication)
print('a * b =',a*b)
## / (division)
print('a / b =',a/b)
## // (floor division)
print('a // b =',a//b)
## % (modulos)
print('a % b =',a%b)
## ** (exponenent)
print('a ** b =',a**b)



##assignement opperators 

## = (Assignement)
print('a =',a)
print('b =',b)
## += (Addition then assignement)
a += b
print('a += b =',a)
## -= (substraction  then assignement)
a -= b
print('a -= b =',a)
## *= (multiplication  then assignement)
a *= b
print('a *= b =',a)
## /= (division  then assignement)
a /= b
print('a /= b =',a)
## //= (floor division  then assignement)
a //= b
print('a//= b =',a)
## %= (modulos  then assignement)
a %= b
print('a %= b =',a)
## **= (exponenent  then assignement)
a **=b
print('a **= b =',a)



##comparaison opperators 

## == (equality)
print('a == b =',a == b)
## != (inequality)
print('a != b =',a != b)
## > (greater than)
print('a > b =',a > b)
## >= (greater than or equal)
print('a >= b =',a >= b)
## < (less than)
print('a < b =',a < b)
## <= (less than or equal)
print('a <= b =',a <= b)



## Logical opperators
print("a = ",a)
print("b = ",b)
## is (true if the variables on both sides of the operator are of the same type false otherwise.)
print('a "is" float =',a is float)
## is not (false if the variables on both sides of the operator are of the same type true otherwise.)
print('a "is not" float =',a is not float)
## in (true if it finds a variable in the specified sequence and false otherwise.)
print('a "in" (1,2,3) =', a in (1,2,3))
## not in (false if it finds a variable in the specified sequence and true otherwise.)
print('a "not in" (1,2,3) =', a not in (1,2,3))
print (a," in binary ==> ",format(int(a),'#b'))
print (b," in binary ==> ",format(int(b),'#b'))
##not (not x, Returns False if x is True,False otherwise)
print ("'not' (a < b)' =", not (a<b))
## or (x or y,  Returns y if x is False, x otherwise  ,note that 0:is fale ,other numbers:true)
print('a "or" b =', a or b)
## and (x and y, Returns x if x is False, y otherwise ,note that 0:is fale ,other numbers:true)
print('a "and" b =', a and b)


## Bitwise opperators (act on operands as if they were strings of binary digits. They operate bit by bit)
print("(Binary) c =",format(c,'#b'))
print("(Decimal) c =",c)
print("(Binary) d =",format(d,'#b'))
print("(Decimal) d =",d)
## & ("BITWISE AND" ==> 0 & 0 = 0 , 0 & 1 = 0 , 1 & 0 = 0 ,  1 & 1 = 1)
print("(Binary) c & d =",format((c & d),'#b'))
print("(Decimal) c & d =",(c & d))
## | ("BITWISE OR" ==> 0 | 0 = 0 , 0 | 1 = 1 , 1 | 0 = 1 ,  1 | 1 = 1)
print("(Binary) c | d =",format((c | d),'#b'))
print("(Decimal) c | d =",(c | d))
## ^ ("BITWISE XOR" ==> 0 ^ 0 = 0 , 0 ^ 1 = 1 , 1 ^ 0 = 1 ,  1 ^ 1 = 0)
print("(Binary) d^c =",format((d^c),'#b'))
print("(Decimal) d^c =",(d^c))
## ~ ("BITWISE NOT" ==> ~0 = 1 , ~1 = 0)
print("(Binary) ~d =",format((~d),'#b'))
print("(Decimal) ~d =",(~d))
## << ("BITWISE LEFT SHIFT" ==> c << 2 = (11001100 << 2) , 1st shift=> 110011000 , 2nd shift => 1100110000)
print("c << 2 =",format((c << 2),"#0b"))
## >> ("BITWISE RIGHT SHIFT" ==> c >> 2 = (11001100 >> 2) , 1st shift=> 01100110 , 2nd shift => 00110011 = 110011)
print("c >> 2=",format((c >> 2), "#0b"))




