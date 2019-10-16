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
