#number guessing game,assign a winning_no,let take a guessing_no from user,if wins print win,if guess low print low,if guess high,print high
wining_no=931
guessing_no=input("user guess a number b/w 1 to 1000")
guessing_no=int(guessing_no)
if wining_no==guessing_no:
    print("winner!! winner!! chicken dinner!!")
else:
    if wining_no<guessing_no:
        print("highhh")
    else:
        print("loww")    
        