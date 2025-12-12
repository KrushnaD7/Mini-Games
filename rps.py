import random
import json


def save_json(filename, data):
    try:
        with open(filename, "r") as f:
            old = json.load(f)
    except:
        old = []

    old.append(data)

    with open(filename, "w") as f:
        json.dump(old, f, indent=4)



def game_rps():
    print("\n--- Rock Paper Scissors ---")
    print("1 = Rock, 2 = Paper, 3 = Scissors, 4 = Exit")

    while True:
        choice = input("Choose (1-4): ")

        if choice == "4":
            print("Returning to main menu...")
            return

        if choice not in ["1", "2", "3"]:
            print("Invalid choice.")
            continue

        player = int(choice)
        computer = random.randint(1, 3)

        mapping = {1: "Rock", 2: "Paper", 3: "Scissors"}

        print("You:", mapping[player])
        print("Computer:", mapping[computer])

        if player == computer:
            result = "Tie"
        elif (player == 1 and computer == 3) or \
             (player == 2 and computer == 1) or \
             (player == 3 and computer == 2):
            result = "Player"
        else:
            result = "Computer"

        print("Winner:", result)

        save_json("rps_results.json", {
            "player": mapping[player],
            "computer": mapping[computer],
            "winner": result
        })



def game_guess():
    print("\n--- Guess the Number (1–100) ---")
    print("Try to guess the number!")
    print("Type 0 to exit.\n")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (1–100): ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess == 0:
            print("Returning to menu...")
            return

        if not (1 <= guess <= 100):
            print("Number must be between 1 and 100.")
            continue

        attempts += 1

        if guess == secret:
            print(f"🎉 Correct! You found it in {attempts} attempts.")
            save_json("guess_results.json", {
                "secret_number": secret,
                "attempts": attempts,
                "status": "win"
            })
            return

        elif guess < secret:
            print("Too small! Try a bigger number.")

        else:
            print("Too big! Try a smaller number.")




def game_ttt():
    print("\n--- Tic Tac Toe ---")
    print("Players choose positions 1–9 using numbers only.")

    board = [" "] * 9
    current = "X"

    def show():
        print()
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")
        print()

    def check():
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a,b,c in wins:
            if board[a] != " " and board[a] == board[b] == board[c]:
                return board[a]
        if " " not in board:
            return "draw"
        return None

    while True:
        show()
        print("1-9 for moves, 0 to exit")
        move = input(f"Player {current}, choose: ")

        if move == "0":
            print("Exiting Tic Tac Toe...")
            return

        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid choice.")
            continue

        move = int(move) - 1

        if board[move] != " ":
            print("Spot taken!")
            continue

        board[move] = current

        result = check()
        if result:
            show()
            if result == "draw":
                print("Draw!")
                save_json("tictactoe_results.json", {"winner": "draw"})
            else:
                print(f"Player {result} wins!")
                save_json("tictactoe_results.json", {"winner": result})
            return

        current = "O" if current == "X" else "X"


# ---------- MAIN MENU ----------
while True:
    print("\n========== GAME MENU ==========")
    print("1 → Rock Paper Scissors")
    print("2 → Guess The Number")
    print("3 → Tic Tac Toe")
    print("4 → Exit")
    print("================================")

    choice = input("Select (1-4): ")

    if choice == "1":
        game_rps()
    elif choice == "2":
        game_guess()
    elif choice == "3":
        game_ttt()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
