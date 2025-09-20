import random

def hand_cricket():
    print("Welcome to Hand Cricket!")
    player_score = 0
    computer_score = 0
    
    # Player bats first
    print("\n--- Your Batting ---")
    while True:
        try:
            player_choice = int(input("Enter your number (1-6): "))
            if not (1 <= player_choice <= 6):
                print("Invalid input. Please enter a number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        computer_bowl = random.randint(1, 6)
        print(f"Computer bowls: {computer_bowl}")

        if player_choice == computer_bowl:
            print(f"OUT! Your final score: {player_score}")
            break
        else:
            player_score += player_choice
            print(f"You scored {player_choice} runs. Current score: {player_score}")

    # Computer bats
    print("\n--- Computer Batting ---")
    print(f"Computer needs to score {player_score + 1} to win.")
    while True:
        computer_bat = random.randint(1, 6)
        try:
            player_bowl = int(input("Enter your bowling number (1-6): "))
            if not (1 <= player_bowl <= 6):
                print("Invalid input. Please enter a number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        print(f"Computer bats: {computer_bat}")

        if computer_bat == player_bowl:
            print(f"OUT! Computer's final score: {computer_score}")
            break
        else:
            computer_score += computer_bat
            print(f"Computer scored {computer_bat} runs. Current score: {computer_score}")
        
        if computer_score > player_score:
            print(f"Computer wins! Computer's final score: {computer_score}")
            break

    # Determine winner
    print("\n--- Game Over ---")
    if player_score > computer_score:
        print("Congratulations! You win!")
    elif computer_score > player_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    hand_cricket()