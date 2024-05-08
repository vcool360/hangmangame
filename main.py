from game_logic import play_hangman

def main():
    print("Welcome to Hangman!")
    guessed, word = play_hangman()
    if "_" not in guessed:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of tries. The word was:", word)

if __name__ == "__main__":
    main()
