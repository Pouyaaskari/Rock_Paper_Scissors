import Menu
import Users
import game
from colorama import Fore

# Printing the main menu
Menu.mainMenu()
# User access to enter desired input
option=input(Fore.BLUE+"Please inter your desired option:")

match option:
    case "1":
        Users.sign_up()
    case "2":
        user = Users.login()
        if user:
            game.start(user)
    case "3":
        Users.getAllUsers()
    case "4":
        exit()
    case _: 
         print(Fore.RED +"Invalid input!,Try again")

    
    
