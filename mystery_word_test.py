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
