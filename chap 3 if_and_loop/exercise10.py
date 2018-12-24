#number guessing game,assign a winning_no,let take a guessing_no from user,if wins print win,if guess low print low,if guess high,print high

import random                                             #this is used to produce random number in python

wining_no=random.randint(1,1000)                           #this will produce random winning no for each new game

guess=1                                                   #used to show guessing time
guessing_no=input("user guess a number b/w 1 to 1000")
guessing_no=int(guessing_no)
game_over= False                                          # working like flag

while not game_over:  #it will give you chance to choose the number again  & again
    if wining_no==guessing_no:
        print(f"winner!! winner!! chicken dinner!!, you guessed on time{guess}")
        game_over= True
    else:
        if wining_no<guessing_no:
            print("highhh")
            guess+=1
            guessing_no=int(input("guess again..>>"))
        else:  
            print("loww") 
            guess+=1
            guessing_no=int(input("guess again..>>"))  

                                                                ##  MODIFIED GUESSING GAME  ##        
