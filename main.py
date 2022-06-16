#****************************************************************
#Name: GOODNEWS AGBADU
#Student Number:A00238219
#
#ANA1001 Mid-Term Project
#****************************************************************

#Importing a package, empty list and assigned variables 
import time
dragon_glasss = 5
health = 100
stock = []
coins = 100

#Defining the function
def start_game():
  '''printing opening statment to start the game'''
  name = input("Enter your Name to start this Game: ")
  print()
  print("Hi "+name +"! Welcome let's get started")
  print()
  while (1):
    print()
    print("Please enter 1 or 2 or 3")
    print()
    print("1. Do you want to Play the Game")
    print()
    print("2. Instrutions")
    print()
    print("3. Exit")
    print()  
    choice = (input("Enter your choice: "));

    if (choice.lower().strip() == '2'):
      print("In life we are faced with different decisions, sometimes conflicting with each other.\nTo survive we need to make smart decisions, remember it either you kill or get killed.\nIn this game, we have 6 rooms, two of the rooms, one has a dragon glass and the other a wildfire.\nTo defeat the Red Eye Dragon in room 5, you need to go through these rooms to get items and kill the Red eye dragon or enter the big black hole.\nRemember you need both the dragon glass and the wildfire to win this game\nIf you win the game, you will collect 100 gold coins that you can spend with friends")
      continue
    elif(choice == '3'):
      print("So sad to see you go at this time we need hero's to defend earth against the Red Eye Dragon")
      break
    elif(choice == '1'):
      print()
      print("Welcome to the Dragon Home")
      print()
    else:
      continue 
    
    room = (input("Please enter room number 1 or 2 to begin your mission: "))

#start of mission 1
    if (room == '1'):
      print(f"\n\nWelcome to room 1\nYour health is at {health}%\nYou have [0] dragon glass\nYou have no wild fire")
      print()
      print("It is dark and cold in here, the red eye dragon could be here: ")
      time.sleep(2)
      print()
      print("you have to collect a wild fire in order to defeat the red eye dragon")
      time.sleep(2)
      print()
      wild_fire = (input("Enter 1 to collect wildfire: "))
      if (wild_fire == '1'):
        print("Searching..........")
        time.sleep(5)
        print("opps....No wild fire in this room")
        time.sleep(2)
        print()
        print("You failed humanity so early")
        print()
        time.sleep(2)
        print("Game Over ")
        time.sleep(2)
        print()
      elif (wild_fire != '1'):
        break
      else:
        break
      play_again = input("Do you want to play again ? (y/n) ")
      if(play_again =='y'):
        print()  
        start_game()
      elif(play_again == 'n'):
        print("Bye...so sad to see you go at this time we need hero's to defend earth against the Red Eye Dragon! ")
        break
      else:
        break
#Start Mission 2
    elif (room == '2'):
      print(f"\n\nWelcome to room 2\nYour health is at {health}%\nYou have [0] dragon glass\nYou have no wild fire")
      print()
      print("It is dark and cold in here, the red eye dragon could be here: ")
      time.sleep(2)
      print()
      print("To stay alive, you have to be smart.:")
      time.sleep(2)
      print()
      print("you have to collect a wild fire in order to defeat the red eye dragon ")
      time.sleep(2)
      print()
      wild_fire = (input("Enter 1 to collect wildfire: "))
      if (wild_fire == '1' ):
        print("Searching......")
        time.sleep(5)
        print("Congratulations......You have collected the wild fire ")
    else:
      print()
      print("sorry..........Try again to save humanity")
      break

    items = (input("\nNow select from room [3] to collect a Dragon Glass: \nSelect [4] to kill the Red Eye Dragon without items.\n "))


#Start Mission 4
    if (items == '4'):
        print
        print(f"\nWelcome to Room 4 \nYour health is at [100%]\nYou have [0]dragon glass\nYou have wildfire\n")
        time.sleep(2)
        print()
        dragon_glass = (input("Enter 1 to collect Dragon glass: "))
        if (dragon_glass == '1'):
          print("Searching..........")
          time.sleep(5)
          print("opps....No Dragon Glass in this room")
          print("You need both dragon glass and wildfire to win this game ")
          print("Game Over ")
          time.sleep(2)
          print()
        elif (dragon_glass != '1'):
          break
        else:
          break
        while ("y"):
          play_again = input("Do you want to play again ? (y/n) ")
          if(play_again =='y'):
            print()
            start_game()
          elif(play_again == 'n'):
            print("Bye...so sad to see you go at this time we need hero's to defend earth against the Red Eye Dragon! ")
            break
          else:
            break
#Start of Mission 3
    if (items == '3'):
        print()
        dragon_glass = (input("Enter 1 to collect Dragon glass :"))
        if (dragon_glass == '1'):
          print("Searching..........")
          time.sleep(5)
          print("Congratulations....you have collected the Dragon Glass in this room")
          time.sleep(2)
          print()
        stock.append("wild fire")
        print(f"\nWelcome to Room 3 \nYour health is at {health}%\nYou have {dragon_glasss} dragon glass\nYou have collected {stock}")
        time.sleep(2)
        print()
        print("Now be ready, you have two rooms (5,6): ")
        time.sleep(2)
        print()
        print("One will lead you to the dragon and the other will lead you to a big dark hole: ")
        time.sleep(2)
        print()
        print("Your decision will determine the fate of humanity: ")
        time.sleep(2)
        print()
    else:
      break
    room6 = (input("To save humanity enter 5 or 6: "))

 #Start Mission 5
    if(room6 == '5'):
        print(f"\n\nWelcome to Room 5\nYour health is at {health}%\nYou have used up your dragon glass\nYou have used all your wild fire")
        print()
        print("You have killed the Red Eye Dragon")
        time.sleep(2)
        print()
        print("You won the game")
        print(f"You have collected {coins} gold coins for saving humanity")
        print("You can spend your gold coins with Goodnews and Adi after python class")
        time.sleep(2)
        break
#Start of Mission 6
    elif(room6 == '6'):
        print("You failed hummanity")
        time.sleep(2)
        print()
        print("Game Over")
        time.sleep(2)
        play_again = input("Do you want to play again ? (y/n) ")
        if(play_again !='y'):
          print("Bye....so sad to see you go at this time we need hero's to defend earth against the Red Eye Dragon!")
          return
#End Game   
    else:
      print()
      print("sorry..........Try again to save humanity")
      break
      time.sleep(2)
start_game()
