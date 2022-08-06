import mongodb
import game
from colorama import Fore
User = mongodb.db.users
def sign_up():
    username=""
    password=""
    while not username:
        username=input(Fore.BLUE + "Please enter userName:")
    try:
        user = User.find_one({"username": username})
    except Exception:
        print(Fore.RED + "Something went wrong")
    if user:
        print(Fore.RED + "User is already exist with this username")
        user = login()
        if user:
            game.start(user)
    while len(password) <= 6:
        password = input(Fore.BLUE + "Please enter your password(The number of characters must be more than 6):")
    try:
        user = User.insert_one({"username": username, "password": password, "name": "", "number_of_wins": 0, "number_of_losses": 0, "win_rate": 0})
        print(Fore.GREEN + "You successfully registered")
    except Exception:
        print(Fore.RED + "Something went wrong")
    print(Fore.LIGHTBLACK_EX + "Login page:")
    user = login()
    if user:
        game.start(user)

def login():
    username=""
    password=""
    user=""
    while not username:
        username=input(Fore.BLUE + "Please enter userName:")
    try:
        user = User.find_one({"username": username})
        if not user:
            print(Fore.RED + "User is not existed please register")
            print(Fore.LIGHTBLACK_EX + "Register page:")
            sign_up()
        else:
            while len(password) <= 6:
                password = input(Fore.BLUE + "Please enter your password(The number of characters must be more than 6):")
            try:
                user = User.find_one({"username":username, "password": password})
                if not user:
                    print(Fore.RED + "please enter valid username and password")
                    print(Fore.BLUE + "Login page:")
                    login()
                else:
                    return user
            except Exception:
                print(Fore.RED + "Something went wrong")
    except Exception:
        print(Fore.RED + "Something went wrong")
    

def getAllUsers():
    for user in User.find():
        print(Fore.GREEN + f"""
        {user["username"]} have gained {user["number_of_wins"]} score
        """)
