"""Code for Binary Search
Author: Martie
Last edited: 31/10-2020
Copyright 2020

PS: This file is for preview-purposes only"""

def main():
    while True:        #Loops the code so you can restart later
        userInput = int(input("Which number shall be guessed? (0-100): "))    #Asks user for a number between 1 and 100
            
        #Variables
        low = 1
        high = 100
        guess = 0
        restart = False

        #Executes code
        try:
            for guesses in range(1, 9):
                guess = int((low + high) / 2)
                print(guess)

                if guess > userInput:
                    high = guess - 1
                elif guess < userInput:
                    low = guess + 1
                elif guess == userInput:
                    print(f"Done! \nFound the number {userInput}. \nGuesses done: {guesses}")
                    break
        #If the user's input in the "userInput" variable was invalid, this code runs
        except TypeError as e:
            print("Error:", e)

            
        #Asks if the user wants to restart
        if restart == False: 
            do_run = input("\nRestart?  y/n: ")
            if do_run == "n":
                break
            elif do_run != "y": 
                print("invalid input")
                continue

        print("\nRestarting... \n")

        if restart == True:
            restart = False

#If the code is ran in *this* file, run main()
if __name__ == "__main__":
    main()
    