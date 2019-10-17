import mystery_word as m


def test_display_word_uppercase():
    assert m.display_word(word="FEATHEREDGED",
                          guesses=['F', 'D']) == "F _ _ _ _ _ _ _ D _ _ D"
    assert m.display_word(word="CAT", guesses=['C']) == "C _ _"


def test_display_word_lowercase():
    assert m.display_word(word="featheredged",
                          guesses=['f', 'd']) == "F _ _ _ _ _ _ _ D _ _ D"


def test_display_word_mixedcase():
    assert m.display_word(word="featheredged",
                          guesses=['F', 'D']) == "F _ _ _ _ _ _ _ D _ _ D"


def test_display_word_all_guesses():
    assert m.display_word(word="CAT", guesses=['C', 'A', 'T']) == "C A T"


def test_is_valid_letter_good_input():
    assert m.is_valid_letter("c")
    assert m.is_valid_letter("Z")


def test_is_valid_letter_multiple_letters():
    assert not m.is_valid_letter("cn")


def test_is_valid_letter_empty_string():
    assert not m.is_valid_letter("")


def test_is_valid_letter_with_nonletters():
    assert not m.is_valid_letter("1")
    assert not m.is_valid_letter('!')


def test_has_been_guessed():
    assert m.has_been_guessed("A",
                              correct_guesses=["A", "T"],
                              incorrect_guesses=["D"])
    assert m.has_been_guessed("A",
                              correct_guesses=["T"],
                              incorrect_guesses=["A", "D"])


def test_has_been_guessed_false():
    assert not m.has_been_guessed(
        "A", correct_guesses=["T", "Z"], incorrect_guesses=["D"])


def test_game_can_be_made():
    game = m.Game(word="beluga")
    assert game.word == "beluga"
    assert len(game.correct_guesses) == 0
    assert len(game.incorrect_guesses) == 0


def test_game_is_not_over_if_no_guesses():
    game = m.Game(word="beluga")
    assert not game.is_game_over()


def test_game_over_from_incorrect_guesses():
    game = m.Game(word="beluga")
    game.incorrect_guesses = ["c", "d", "f", "h", "i", "j", "k", "m"]
    assert game.is_game_over()

    game.incorrect_guesses.append("z")
    assert game.is_game_over()


def test_game_over_from_correct_guesses():
    game = m.Game(word="beluga")
    game.correct_guesses = ["b", "e", "l", "u", "g", "a"]
    assert game.is_game_over()


def test_have_all_letters_been_guessed_true():
    game = m.Game(word="beluga")
    game.correct_guesses = ["b", "e", "l", "u", "g", "a"]
    assert game.have_all_letters_been_guessed()


def test_add_guess_adds_correct_guess():
    game = m.Game(word="beluga")
    game.add_guess("b")
    assert len(game.correct_guesses) == 1
    assert len(game.incorrect_guesses) == 0


def test_add_guess_adds_correct_guess_case_insensitive():
    game = m.Game(word="beluga")
    game.add_guess("B")
    assert len(game.correct_guesses) == 1
    assert len(game.incorrect_guesses) == 0


def test_add_guess_adds_incorrect_guess():
    game = m.Game(word="beluga")
    game.add_guess("d")
    assert len(game.correct_guesses) == 0
    assert len(game.incorrect_guesses) == 1
