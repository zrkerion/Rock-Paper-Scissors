
#import a random module 
import random

#Import sys for exit
import sys 

def game_instructions():
  print ("\033[1m Rules of the Rock, paper, and scissor game as follows: \033[0m \n"
 "\n"
 "rock  VS paper     -> Paper wins \n" 
 "rock  VS scissors  -> Pock wins \n" 
 "paper VS scissors  -> Scissors wins \n \n ")

def play_game():
 print ("\n \033[1m Pick one of the following options: \033[0m \n"
 "------------------------------------------------------\n"
 "\033[1m1.\033[0m Rock \n"
 "\033[1m2.\033[0m Paper \n"
 "\033[1m3.\033[0m Scissors \n"
 "------------------------------------------------------\n") 
 
 #Loop
 while True: 
    try:  
    # take the input from user 
     pick = int(input ("Enter pick: \n")) -1
     #print (pick)
     if pick > 2 or pick < 0:
       print("\nError! Enter a valid pick! \n")
      
     else:
       break

    except:
     print ("Error! Enter a valid pick! \n")
      
  #validator message        
  #print ("\nSuccess!")

 if  pick == 0:
     pick_name = 'Rock'
 elif pick == 1:
     pick_name = 'Paper'
 else:   
      pick_name = 'Scissors' 
 

 #Print user pick
 print ("\nYour pick is: " + "\033[1m" + pick_name +"\033[0m")
 
 #print("\nNow its computers turn...")
 pc_list = ["Rock", "Paper", "Scissors"]
 
 random_number = random.randint(0,2)

 print("\nComputer pick is: " + (pc_list[random_number]))
 
 if pick == 0 and random_number == 0 or pick == 1 and random_number == 1 or pick == 2 and random_number == 2:
  print("\n--------- \033[1m It´s a draw!\033[0m ---------")
 elif pick == 0 and random_number == 1 or pick == 1 and random_number == 2 or pick == 2 and random_number == 0:
  print("\n---------- \033[1m You lose! \033[0m ----------")
 else:
  print("\n---------- \033[1m You win! \033[0m -----------")


 while True:   
   pick_yn = input ("\nWould you like to play again? Y/N \n")  
   #Play again?
   if pick_yn == "Y" or pick_yn == "y":
     play_game()
     print("\n")
     
   elif pick_yn == "N" or pick_yn == "n":      
     print('\n---\033[1m Get out of my swamp! \033[0m---')
     sys.exit("\nGame Closed. \n")
  
   else:
     print ("\nEnter a valid option!\n") 



#Game instrucions duh
game_instructions()

#Start the game
play_game()
