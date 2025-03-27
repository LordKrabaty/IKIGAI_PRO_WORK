"""Module for testing functions in the ikidef and drawdef modules."""

from src import ikidef, drawdef
import pytest

# USER DATA -----------------------------------------------------------------------------------

def test_first_word():
    """Test the first_word function."""
    assert ikidef.first_word('te_xt test tets lets', ' ') == 'te_xt'
    assert ikidef.first_word('text', ' ') == 'text'
    assert ikidef.first_word('', ' ') == ''


def test_current_date():
    """Test the current_date function."""
    len_date = len(ikidef.current_date())
    assert len_date == 10  # Check proper length of the date string.
    dot_in_date = '.' in ikidef.current_date()
    assert dot_in_date is True  # Check if there is a dot in the date string.
    dots = ikidef.current_date().count('.')
    assert dots == 2  # Ensure there are exactly two dots in the date string.


###################### QUESTIONNAIRE #######################################

def test_is_it_number():
    """Test the is_it_number function."""
    assert ikidef.is_it_number(5, 'e') == 5  # Test with an integer.
    assert ikidef.is_it_number(5.5, 'e') == 5.5  # Test with a float.
    assert ikidef.is_it_number('5,55', 'e') == 5.55  # Test with a string containing a comma.
    assert ikidef.is_it_number('five', 'e') == 'e'  # Test with an invalid string.


def test_true_or_not():
    """Test the true_or_not function."""
    assert ikidef.true_or_not(5, 5) is True
    assert ikidef.true_or_not(10, 5) is True
    assert ikidef.true_or_not(4, 5) is False
    assert ikidef.true_or_not(-5, 5) is False
    with pytest.raises(TypeError):
        ikidef.true_or_not('five', 5)
        ikidef.true_or_not('five', 'five')



###################### DRAW #######################################

def test_max_line_length():
    """Test the max_line_length function."""
    text = 'lin1 lin2 lin3 lin4'
    text4 = 'lin1\n\tlin2\n\tlin3\n\tlin4'
    text10 = 'lin1 lin2\n\tlin3 lin4'
    assert drawdef.max_line_length(text, 4) == text4
    assert drawdef.max_line_length(text, 10) == text10  # 'lin1 lin2 ' = 10 characters.
    assert drawdef.max_line_length(text, len(text)) == text
