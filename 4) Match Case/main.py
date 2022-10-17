"""
------------------------PYTHON FULL COURSE-----------------------------------
-----------------------------------------------------------------------------
"""


"""
------------------------MATCH CASE-----------------------------------
"""

##get user input (in lower case to avoid any confusions with user input!0
user_input = str(input("what's is the month of your birthday? ")).lower()

##match cases with user input
match user_input:
    case "january":
        print('winter babies might be surprisingly athletic !')
    case "february":
        print('Research shows that babies born this time of year are less irritable than those who arrive at other times.')
    case "march":
        print('Why are March babies more likely to become CEOs than their peers?')
    case "april":
        print('Research shows that April babies tend to be half-glass-full types. ')
    case "may":
        print('People born in May consider themselves luckier than those born in other months. ')
    case "june":
        print('Short or tall: Which end of the spectrum do most June babies fall?')
    case "july":
        print('Are July babies really more likely to have a “sunny disposition?”')
    case "August":
        print('Two things that Barack Obama, Bill Clinton, and Lyndon B. Johnson have in common: They were all born in August and all presidents.')
    case "september":
        print('More babies are born on September 9th than any other day of the year!')
    case "october":
        print('Babies born in October are more likely to make it to the big 100 than those born in other months. ')
    case "november":
        print('November kids tend to be BIGGER')
    case "december":
        print('Congrats! Research shows that December babies tend to have fewer tantrums than the rest!')
    case _: ##default case !
        print("error, you entered a wrong Month !!!")
