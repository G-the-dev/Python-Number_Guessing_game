# NUMBER GUESSING GAME

import random
N = input('Type a number: ')

if N.isdigit():
    N = int(N)
    
    if N <= 0:
        print('Invalid Entry!!')
        print('Please re-enter the number > 0.')
        
else:
    print('Please type a number next time.')
    quit()
    
ran_num=random.randrange(0,N)
guesses=0

while True:
    guesses += 1
    G = input('Make a guess: ')
    if G.isdigit():
        G = int(G)
    else:
        print('Please type a number next time.')
        continue
    
    if G == ran_num:
        print('You got it right :)')
        break
        
    elif G > ran_num:
        print("You are above the guess number!")

    elif G < ran_num:
        print("You are below the guess number!")
    # else:
    #     print('You got it wrong :(')
        
print("Not bad! You got it in", guesses, "guesses")
print('This is the random number: ',ran_num)