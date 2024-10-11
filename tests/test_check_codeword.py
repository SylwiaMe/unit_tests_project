from lib.check_codeword import *

def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_with_first_and_last_right_letter():
    result = check_codeword('hippie')
    assert result == "Close, but nope."

def test_with_the_incorrect_codeword():
    result = check_codeword("Cabbage")
    assert result == "WRONG!"
    