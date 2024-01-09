import random
MIN_NUM = 1
MAX_NUM = 101

#random bomb number
bomb_number = random.randint(MIN_NUM, MAX_NUM)
guesses = 0

min_temp = MIN_NUM
max_temp = MAX_NUM - 1
min_bomb = bomb_number - 1
max_bomb = bomb_number + 1

print('\nBOMB GAME!')
print('Choose a number between 1-100')
print('=============================')

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    
    #got the bomb = lose
    if user_guess == bomb_number:
        print("\nBBBBBOOOOOOOOOOMMMMMMMMMMMMMMMM!!!!!!!!!")
        print("You lose!")
        print("You got the bomb number:",bomb_number,"in", guesses, "guesses","\n")
        break
    #user choose number lower or higher than the range
    elif user_guess <= min_temp or user_guess >= max_temp :
        print("Please choose a number between",min_temp, "-",max_temp,"\n") 
    #user choose number higher than the bomb
    elif user_guess > bomb_number:
        max_temp = user_guess
        print("The bomb number is between",min_temp, "-",user_guess,"\n")
    #user choose number lower than the bomb
    elif user_guess < bomb_number:
        min_temp = user_guess
        guesses -= 1
        print("The bomb number is between",user_guess, "-",max_temp,"\n")
    #nobody pick the bomb
    if min_temp == min_bomb < bomb_number < max_temp == max_bomb:
         print("You win! The bomb number is ",bomb_number,"\n")
         break
    
