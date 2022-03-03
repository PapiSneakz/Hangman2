while True:
    number = 0
    hangman = ["\t +--------+","\t |       | |","\t {}       | |","\t{}{}{}      | |","\t {}       | |","\t{} {}      | |","\t         | |","  _______________|_|___","  `````````````````````"]
    print("------------------------------------------")
    print("WELCOME TO HANGMAN")
    for i in hangman:
        print(hangman[number])
        number+=1
    print("------------------------------------------")

    wordInput = input("The word: ")

    while not wordInput.isalpha():
        wordInput = input("The word can only contain letters: ")

    for i in range(30):
        print(" ")

    print("The word consists of " + str(len(wordInput)) + " letters")

    guess = input("Guess the word: ")
    guesses = 0


    while True:
        try:
            if guess != wordInput:
                print("                                                                             " + hangman[guesses])
                guess = input("Wrong: ")
                guesses+= 1
            if guess == wordInput:
                print("You won")
                break
        except:
            print("You dont have any guesses you lose")
            break
        
    response = input("Do you wanna play again? (Type yes or no): ")
    response.lower()
    if response == "yes":
        for i in range(25):
            print(" ")
    if response != "yes":
        print("Okay bye")
        break
