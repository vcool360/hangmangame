def update_guessed(guess, word, guessed):
    return "".join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
