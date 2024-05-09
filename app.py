from flask import Flask, render_template, request, session, redirect, url_for
from word_fetcher import get_random_word
from game_logic import update_guessed

app = Flask(__name__)
app.secret_key = 'your_secure_secret_key'  # Use a secure key in production

# Hangman stages for visualization
HANGMAN_PICS = [
    """
   +---+
   |   |
       |
       |
       |
       |
=========""", """
   +---+
   |   |
   O   |
       |
       |
       |
=========""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""", """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""", """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========""", """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""", """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
========="""]

def initialize_game():
    session['word'] = get_random_word()
    session['guessed'] = "_" * len(session['word'])
    session['tries'] = 6
    session['guessed_letters'] = []
    session['hangman_visual'] = HANGMAN_PICS[0]
    session['message'] = ''

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'guessed_letters' not in session or 'hangman_visual' not in session:
        initialize_game()

    if request.method == 'POST':
        guess = request.form.get('letter', '').lower()
        if len(guess) == 1 and guess.isalpha():
            if guess not in session['guessed_letters']:
                session['guessed_letters'].append(guess)
                if guess not in session['word']:
                    session['tries'] -= 1
                    session['hangman_visual'] = HANGMAN_PICS[6 - session['tries']]
                    if session['tries'] <= 0:
                        session['message'] = f"Sorry, you lost! The word was '{session['word']}'."

                else:
                    session['guessed'] = update_guessed(guess, session['word'], session['guessed'])
                    if '_' not in session['guessed']:
                        session['message'] = f"Congratulations, you won! The word was '{session['word']}'."

    return render_template('index.html', guessed=session['guessed'], tries=session['tries'],
                           guessed_letters=session['guessed_letters'], hangman_visual=session['hangman_visual'],
                           message=session['message'])

@app.route('/restart', methods=['POST'])
def restart():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)