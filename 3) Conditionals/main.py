"""
------------------------PYTHON FULL COURSE-----------------------------------
-----------------------------------------------------------------------------
"""


"""
------------------------CONDITIONALS-----------------------------------
"""

#(random) module allows to choose stuffs randomly
import random

print("1) Paper  2) Rock 3) Sicors")

##get user input (as integer value, it is string by default!)
user_input = int(input("give your choice (1 , 2, 3)?"))

##choose random integer "x" ( 1 =< x < 4)
com_input = random.randrange(1,4)

if (user_input not in (1,2,3)):
	print("invalid input !!!")
else:
	if (com_input == user_input):
		print("Draw")
	elif ((com_input == 1) & (user_input == 2)):
		print("Com chosed Paper \n==> Com wins")
	elif ((com_input == 1) & (user_input == 3 )):
		print("Com chosed Paper \n==> You wins")
	elif ((com_input == 2) & (user_input == 1 )):
		print("Com chosed Rock \n==> You wins")
	elif ((com_input == 2) & (user_input == 3)):
		print("Com chosed Rock \n==> Com wins")
	elif ((com_input == 3) & (user_input == 1 )):
		print("Com chosed Sicors \n==> Com wins")
	elif ((com_input == 3) & (user_input == 2)):
		print("Com chosed Sicors \n==> You wins")	
