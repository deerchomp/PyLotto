import random

def giveRules():
    print("Welcome to lottery!\n\n")
    print("Both correct in order wins $10,000!")
    print("Both digits in any order $3,000!")
    print("One digit correct wins $1,000!\n")

def getGuess():
    guess = int(input("Enter a number to begin. Good Luck!\n\n"))
    return guess

def calc(guess):
    win = random.randint(0,99)
    guessdig1 = guess // 10
    guessdig2 = guess % 10
    num1 = win // 10
    num2 = win % 10
    return guessdig1, guessdig2, num1, num2, win

def giveResults(guess, guessdig1, guessdig2, num1, num2, win):
    if guess == win:
        print("You won $10,000! The number was: ",win)
    elif guessdig2 == num1 and guessdig1 == num2:
        print("You won $3,000! The number was: ",win)
    elif guessdig1 == num1 or guessdig1 == num2:
        print("You won $1,000! The number was: ",win)
    elif guessdig2 == num1 or guessdig2 == num2:
        print("You won $1,000! The number was: ",win)
    else:
        print("Sorry, try again. The number was: ",win)

def main():
    play = 'y'
    while play == 'y':
        giveRules()
        guess = getGuess()
        g1, g2, n1, n2, w = calc(guess)
        giveResults(guess, g1, g2, n1, n2, w)
        play = input("Would you like to play again? 'y' or 'n'")
          
main()
