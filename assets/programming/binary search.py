"""Code for Binary Search
Author: Martie
Last edited: 31/10-2020
Copyright 2020"""

def main():
    while True:        #Looper koden så man kan restarte senere
        userInput = int(input("Hvilket tall skal maskinen gjette? (0-100): "))    #Spør bruker om et tall mellom 1 og 100
            
        #Variabler
        low = 1
        high = 100
        guess = 0
        restart = False

        #Utfører kode
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
        #Hvis bruker skrev inn noe tull i variabelen "userInput", kjører denne koden
        except TypeError as e:
            print("Error:", e)
            
        #Kode som spør om du vil starte på nytt
        if restart is False: 
            do_run = input("\nRestart?  y/n: ")
            if do_run == "n":
                break
            elif do_run != "y": 
                print("invalid input")
                continue

        print("\nRestarting... \n")

        if restart == True:
            restart = False

#Hvis koden blir kjørt i *denne* filen, kjør main()
if __name__ == "__main__":
    main()
    