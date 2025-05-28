from random import randint

def start_game():
    print("Welcome to Rock, Paper, Scissors!")
    print('How many players are playing? (1 or 2)')
    NumOfPlayers = input().strip()
    play_round(NumOfPlayers)

def play_round(NumOfPlayers='1'):
    print(f"new round with {NumOfPlayers} player(s)")
    Message = f"Choose your move: Rock (R), Paper (P), or Scissors (S): "
    print(Message)
    UserChoice = input().strip().upper()
    if NumOfPlayers == '2':
        print("Player 2, please make your choice.")
        Player2Choice = input().strip().upper()
        game_logic(UserChoice, Player2Choice, NumOfPlayers)
    else:
        show_player_choice(UserChoice)
        game_logic(UserChoice)

def show_player_choice(Choice):
    if Choice == 'R':
        print("You chose Rock!")
    elif Choice == 'P':
        print("You chose Paper!")
    elif Choice == 'S':
        print("You chose Scissors!")
    else:
        print("Invalid Choice. Please choose Rock (R), Paper (P), or Scissors (S).")
        play_round()
        return

def game_logic(FirstChoice, SecondChoice=None, NumOfPlayers='1'):
    if SecondChoice is None:
        SecondChoice = computer_choice()

    if FirstChoice is None or not FirstChoice:
        print("No Choice was made.")
        play_round()
        return
    
    if FirstChoice == SecondChoice:
        print("It's a tie!")
    
    elif FirstChoice == 'R' and SecondChoice != 'P':
        print("You win! Rock crushes Scissors.")
        print("Player 1 Wins!")

    elif FirstChoice == 'P' and SecondChoice != 'S':
        print("You win! Paper covers Rock.")
        print("Player 1 Wins!")
    
    elif FirstChoice == 'S' and SecondChoice != 'R':
        print("You win! Scissors cut Paper.")
        print("Player 1 Wins!")
    else:
        print(f"You lose player 1 chose {show_abrv(FirstChoice)} and player 2 chose {show_abrv(SecondChoice)} ! Better luck next time.")
        print("Player 2 Wins!")
    
    keep_playing(NumOfPlayers)

def show_abrv(Choice):
    if Choice == 'R':
        return "Rock"
    elif Choice == 'P':
        return "Paper"
    elif Choice == 'S':
        return "Scissors"
    else:
        return "Invalid Choice"

def keep_playing(NumOfPlayers):
    Choice = input("Do you want to play again? (Y/N): ").strip().upper()
    if Choice != 'Y':
        print("Thanks for playing!")
        return False
    else:
        print("Starting a new round...")
        play_round(NumOfPlayers)
        return True

def computer_choice():
    choices = ['R', 'P', 'S']
    return choices[randint(0, 2)]


start_game()