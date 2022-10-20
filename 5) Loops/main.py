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


print("------------------------WHILE LOOP------------------------")

print("------------------------SIMPLE GUESS THE NUMBER GAME USING WHILE LOOP------------------------")

import random 

is_correct = False ##to check if user guessed the right number

total_attempts = 5 ## total attempts

nb_attemps = 0 ## to count the number of attempts

correct_answer = random.randint(0,10) ##the correct answer

##describe the game to user
print(f"Guess a number from (0 to 10), 'You only have {total_attempts} attemps'\n")

## while (is_correct is False) "solution is not correct" and (nb_attempts < total attempts) keep giving chances to user
## we exit the loop in 1 of 2 situations
## 1st situation : (is_correct is True) "solution is correct" ,so the users wins here
## 2nd situation : (nb_attempts >= total attempts) ,so the user loses
while(is_correct == False and nb_attemps < total_attempts):
    
    ##at each iteration we increment the nb_attemps
    nb_attemps = nb_attemps + 1
    
    ##get the user guess
    user_number = int(input(f"'{total_attempts-(nb_attemps-1)} attemp(s) left', Enter your number ? "))
    
    ##check the user guess
    if(user_number == correct_answer):
        print(f"You guessed it in {nb_attemps} attempt(s) !!! \n") 
        is_correct = True
    else:
        if(nb_attemps < total_attempts):
            print("Wrong  ,Guess Again !!! \n")


##case if user wins
if(is_correct == True):
    print(f"\nYou Win !!! the answer is {correct_answer}")

##case if user loses
if(nb_attemps > (total_attempts-1)):
    print(f"\nYou Lose !!! the answer is {correct_answer}")



