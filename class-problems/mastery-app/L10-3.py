# Modify the script so that it picks a number between 0 and 1000
# and it counts how many guesses they make.  
# If they can't get it in 10 guess, then tell them they've lost;
# else say they won ...

# (Hint: look up the keyword "break" in Python)

def guessing_game():
    answer = randint(0,1000)
    print('I am thinking of a number in the range 0 to 1000')
    print('try to guess it')
    guess = int(input('> '))
    count = 0
    while guess != answer:
        if count > 10:
            break
        if guess<answer:
            print(guess,'is too low. Try again.')
        elif guess>answer:
            print(guess,'is too high. Try again.')
        guess = int(input('> '))
        count = count + 1
    
    if count>10:
        print('you lose!')
    elif count<10:
        print('you win!')