from random import randint

def start_game():
    print("Welcome to Rock, Paper, Scissors!")
    print('How many players are playing? (1 or 2)')
    num_of_players = input().strip()
    play_round(num_of_players)

def play_round(num_of_players='1'):
    print(f"new round with {num_of_players} player(s)")
    message = f"Choose your move: Rock (R), Paper (P), or Scissors (S): "
    print(message)
    user_choice = input().strip().upper()
    if num_of_players == '2':
        print("Player 2, please make your choice.")
        player_two_choice = input().strip().upper()
        game_logic(user_choice, player_two_choice, num_of_players)
    else:
        show_player_choice(user_choice)
        game_logic(user_choice)

def show_player_choice(choice):
    if choice == 'R':
        print("You chose Rock!")
    elif choice == 'P':
        print("You chose Paper!")
    elif choice == 'S':
        print("You chose Scissors!")
    else:
        print("Invalid choice. Please choose Rock (R), Paper (P), or Scissors (S).")
        play_round()
        return

def game_logic(first_choice, second_choice=None, num_of_players='1'):
    if second_choice is None:
        second_choice = computer_choice()

    if first_choice is None or not first_choice:
        print("No choice was made.")
        play_round()
        return
    
    if first_choice == second_choice:
        print("It's a tie!")
    
    elif first_choice == 'R' and second_choice != 'P':
        print("You win! Rock crushes Scissors.")
        print("Player 1 Wins!")

    elif first_choice == 'P' and second_choice != 'S':
        print("You win! Paper covers Rock.")
        print("Player 1 Wins!")
    
    elif first_choice == 'S' and second_choice != 'R':
        print("You win! Scissors cut Paper.")
        print("Player 1 Wins!")
    else:
        print(f"You lose player 1 chose {show_abrv(first_choice)} and player 2 chose {show_abrv(second_choice)} ! Better luck next time.")
        print("Player 2 Wins!")
    
    keep_playing(num_of_players)

def show_abrv(choice):
    if choice == 'R':
        return "Rock"
    elif choice == 'P':
        return "Paper"
    elif choice == 'S':
        return "Scissors"
    else:
        return "Invalid choice"

def keep_playing(num_of_players):
    choice = input("Do you want to play again? (Y/N): ").strip().upper()
    if choice != 'Y':
        print("Thanks for playing!")
        return False
    else:
        print("Starting a new round...")
        play_round(num_of_players)
        return True

def computer_choice():
    choices = ['R', 'P', 'S']
    return choices[randint(0, 2)]


start_game()