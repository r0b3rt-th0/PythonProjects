import random

def rockPaperScissors(user_input, computer_input):
    if((user_input == "rock") & (computer_input == "rock")):
        print("The computer threw rock. Rock and rock ends in a draw.")
    elif((user_input == "scissor") & (computer_input == "scissor")):
        print("The computer threw scissor. Scissor and scissor ends in a draw.")
    elif((user_input == "paper") & (computer_input == "paper")):
        print("The computer threw paper. Paper and paper ends in a draw.")
    
    elif((user_input == "rock") & (computer_input == "paper")):
        print("The computer threw paper. Paper beats rock, computer wins.")
    elif((user_input == "scissor") & (computer_input == "rock")):
        print("The computer threw rock. Rock beats scissor , computer wins.")
    elif((user_input == "paper") & (computer_input == "scissor")):
        print("The computer threw scissor. Scissor bearts paper, computer wins.")

    elif((user_input == "rock") & (computer_input == "scissor")):
        print("The computer threw scissor. Rock beats scissor, User wins.")
    elif((user_input == "scissor") & (computer_input == "paper")):
        print("The computer threw paper. Scissor beats paper , User wins.")
    elif((user_input == "paper") & (computer_input == "rock")):
        print("The computer threw rock. Paper beats rock, User wins.")

rock = "rock"
scissor = "scissor"
paper = "paper"
 
list = [rock, paper, scissor]

computer = random.choice(list)

user = input ("Rock. Paper. Scissor. Shoot!: ")

rockPaperScissors(user, computer)
    
prompt = input("Would you like to play Rock Paper, Scissor again? Y/N: ")

prompt = prompt.upper()

while prompt == 'Y':
    user = input("Rock. Paper. Scissor. Shoot!: ")
    rockPaperScissors(user, computer)
    print()
    prompt = input("Would you like to play Rock Paper, Scissor again? Y/N: ")
    prompt = prompt.upper()
