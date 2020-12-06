import random

def print_hello() :
    print("  The Little Giraffe game    .-\",")
    print("  Version : 0.0.1            `~||")
    print("                               ||___")
    print("  Powered by KonstantIMP       (':.)`")
    print("                               || ||")
    print("  Feedback email :             || ||")
    print("  mihedovkos@gmail.com         ^^ ^^")
    print()

def print_help() :
    print("  Game Rules ________________")
    print("    The Little Giraffe will make a number from 0 to 100")
    print("    You need to guess this number. You enter the number")
    print("    you think  the girrafe made. The Little Giraffe can")
    print("    tell you one of these phrases : \"Your number is too")
    print("    big\", \"Your number is too small\" and \"It`s correct\"")
    print("  ___________________________")
    print()
    
def yes_no_enter() :
    while True :
        answer = input()
        
        print()
        
        if answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes" : return True
        elif answer == "N" or answer == "n" or answer == "No" or answer == "no" : return False
        else :
            print("  Sorry! Incorrect input! Try again [(Y)es/(N)o] : ", end='')
    
def print_bye() :
    print("  Visit us again!!!")
    print("  Bye")
    
def play_game() :
    num = random.randint(0, 100)
    enters = 0
    
    print("  The Little Giraffe made a number. HiHiHi")
    print("  You can guess the number in just 7 tries. Try it!")
    print()
    
    while True :
        n = int(input("  Enter your num : "))
        enters = enters + 1
        
        if n == num :
            print("  You are absolutly right!!!")
            print("  It took you", enters, "tries to guess the number")
            print()
            return
        if n > num :
            print("  Your number is too big...")
        else :
            print("  Your number is too small...")
    
if __name__ == "__main__" :
    print_hello()
    print_help()
    
    print("  Do you want to play the game? [(Y)es/(N)o] : ", end='')
    
    if yes_no_enter() == True :
        while True :
            play_game()
            
            print("  Do you want to play the game again? [(Y)es/(N)o] : ", end='')
            if yes_no_enter() == False : break
        
    print_bye()
    
