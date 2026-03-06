import random

print("Welcome to Rock, Paper, Scissors!")
print("==================")
print("1. ✊ Rock"
    "\n2. ✋ Paper"
    "\n3. ✌️ Scissors")

player_choice = int(input("Please select your move: "))
computer_choice = random.randint(1, 3)

#player choice input
if player_choice == 1:
    print("You chose: ✊ Rock")
elif player_choice == 2:
    print("You chose: ✋ Paper")
elif player_choice == 3:
    print("You chose: ✌️ Scissors")

#computer choice random.randint
if computer_choice == 1:
    print("Computer chose: ✊ Rock")
elif computer_choice == 2:
    print("Computer chose: ✋ Paper")
elif computer_choice == 3:
    print("Computer chose: ✌️ Scissors")

#determine the winner
if player_choice == 1 and computer_choice == 3 or player_choice == 2 and computer_choice == 1 or player_choice == 3 and computer_choice == 2:
    print("You win!")
elif player_choice == computer_choice:
    print("It's a tie!")
else:
    print("Computer wins!")