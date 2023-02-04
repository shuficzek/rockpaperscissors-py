import random #Importing random.
import time #Importing time.
game = ["Rock", "Paper", "Scissors"] #Words that gonna be selected.
print ("Game rock paper scissors.") #Showing title of the game.
for i in range(25): #How many times will this commands be executed.
    randomword = random.choice(game) #Selecting words from variable.
    time.sleep(2) #Waiting every time when word gonna show up.
    print(randomword) #Showing selected word.
