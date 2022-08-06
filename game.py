import mongodb
import random
from colorama import Fore
User = mongodb.db.users

def start(user):
    number_of_wins = user["number_of_wins"]
    number_of_losses=user["number_of_losses"]
    win_rate = user["win_rate"]
    choices=["rock","paper","scissors"]
    print(Fore.YELLOW + str(choices))
    while True:
        user_choice=input(Fore.BLUE +"Please enter a value from choices (Press q for exit)=> ").lower()
        if user_choice == "q":
            break
        if user_choice not in choices:
            print(Fore.RED +"Invalid input!,Try again")
            continue

        random_choice=random.randint(0,2)
        computer=choices[random_choice]
        print(Fore.YELLOW + f"Computer selection is ==> {computer}")

        if user_choice==computer:
            print(Fore.MAGENTA + f"Tie! Start again")

        elif user_choice == "rock" and computer == "scissors":
            print(Fore.GREEN + f"Great! You win =) | +1 score")
            number_of_wins+=1

        elif user_choice == "paper" and computer == "rock":
            print(Fore.GREEN + f"Great! You win =) | +1 score")
            number_of_wins+=1
                
        elif user_choice == "paper" and computer == "rock":
            print(Fore.GREEN + f"Great! You win =) | +1 score")
            number_of_wins+=1

        elif user_choice == "scissors" and computer == "paper":
            print(Fore.GREEN + f"Great! You win =) | +1 score")
            number_of_wins+=1

        else:
            print(Fore.RED + "Sorry! You Lost | -1 score")
            number_of_losses+=1
        if number_of_losses != 0:
            win_rate = number_of_wins / number_of_losses
        User.update_one({"_id": user["_id"]}, { "$set": { "number_of_wins": number_of_wins, "number_of_losses": number_of_losses, "win_rate": win_rate } })

    print(Fore.GREEN + f"{number_of_wins} times you win!")
    print(Fore.RED + f"{number_of_losses} times computer win!")
    print(Fore.MAGENTA + f"{win_rate} your win rate!")
