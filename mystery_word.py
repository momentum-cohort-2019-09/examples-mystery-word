import string


def display_word(word, guesses):
    word = word.upper()
    guesses = [guess.upper() for guess in guesses]
    display_letters = []
    for letter in word:
        if letter in guesses:
            display_letters.append(letter)
        else:
            display_letters.append('_')
    return " ".join(display_letters)


def is_valid_letter(user_input):
    return len(user_input) == 1 and user_input in string.ascii_letters


def has_been_guessed(letter, correct_guesses, incorrect_guesses):
    return letter in correct_guesses + incorrect_guesses


class Game:

    def __init__(self, word):
        self.word = word
        self.correct_guesses = []
        self.incorrect_guesses = []
        self.max_incorrect_guesses = 8

    def is_game_over(self):
        if self.have_all_letters_been_guessed():
            return True
        return len(self.incorrect_guesses) >= self.max_incorrect_guesses

    def have_all_letters_been_guessed(self):
        # alternative
        # return all([letter in self.correct_guesses for letter in self.word])

        for letter in self.word:
            if letter not in self.correct_guesses:
                return False
        return True

    def add_guess(self, guess):
        """Given a guessed letter, add it to correct or incorrect guesses."""
        guess = guess.lower()
        if guess in self.word.lower():
            self.correct_guesses.append(guess)
        else:
            self.incorrect_guesses.append(guess)

    def get_user_guess(self):
        while True:
            guess = input("What is your guess? ")
            if is_valid_letter(guess):
                return guess
            print("That's not a valid answer!")

    def run(self):
        print("Welcome to Mystery Word!")

        while not self.is_game_over():
            print(
                f"You have {self.max_incorrect_guesses - len(self.incorrect_guesses)} guesses left."
            )
            print(display_word(self.word, self.correct_guesses))
            guess = self.get_user_guess()
            self.add_guess(guess)
            if self.is_game_over():
                if self.have_all_letters_been_guessed():
                    print("You won!")
                else:
                    print("You are the loser!")

    def __repr__(self):
        return f"<Game word={self.word}>"


if __name__ == "__main__":
    game = Game("beluga")
    game.run()
