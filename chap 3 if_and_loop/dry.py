# dry principle,go downward bro...!!
#number guessing game,assign a winning_no,let take a guessing_no from user,if wins print win,if guess low print low,if guess high,print high
wining_no=931
guess=1 #used to show guessing time
guessing_no=input("user guess a number b/w 1 to 1000")
guessing_no=int(guessing_no)
game_over= False
while not game_over:  #it will give you chance to choose the number again  & again
    if wining_no==guessing_no:
        print(f"winner!! winner!! chicken dinner!!, you guessed on time{guess}")
        game_over= True
    else:
        if wining_no<guessing_no:
            print("highhh")     
        else:  
            print("loww") 
           
        guess+=1                                       # DRY MEANS DONT REPEAT YOURSELF
        guessing_no=int(input("guess again..>>"))      #LINE 17 AND 18 BOTH NEEDE FOR HIGHH AND LOWW CONDITION,SO WE ARE TAKING THOSE STATEMENT ONCE,ITS DRY PRINCIPLE
                                                       # MORE: WATCHING THE DIFF B/W THIS CODE AND ORIGINAL CODE CHECK exercise10.py  



                                                                ##  MODIFIED GUESSING GAME  ##        
