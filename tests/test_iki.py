"""Module for testing functions in the ikidef and drawdef modules."""

from src import ikidef, drawdef
import pytest

# USER DATA -----------------------------------------------------------------------------------


def test_first_word_basic_cases():
    """
    Test the first_word function with typical cases, including strings with separators 
    and strings without separators.
    """
    # Test with a separator present in the middle of the text
    text = "hello-world"
    separator = "-"
    assert ikidef.first_word(text, separator) == "hello"

    # Test with no separator in the text
    text = "helloworld"
    separator = "-"
    assert ikidef.first_word(text, separator) == "helloworld"

    # Test with a separator at the beginning of the text
    text = "-world"
    separator = "-"
    assert ikidef.first_word(text, separator) == ""

def test_first_word_edge_cases():
    """
    Test the first_word function with edge cases such as empty strings, 
    single-character separators, and multi-character separators.
    """
    # Test with an empty text
    text = ""
    separator = "-"
    assert ikidef.first_word(text, separator) == ""

    # Test with a single character text matching the separator
    text = "-"
    separator = "-"
    assert ikidef.first_word(text, separator) == ""

    # Test with a multi-character separator
    text = "hello_world_example"
    separator = "_world_"
    assert ikidef.first_word(text, separator) == "hello"

def test_first_word_special_characters():
    """
    Test the first_word function with special characters as separators 
    and text containing unusual formatting.
    """
    # Test with a special character separator
    text = "hello@world"
    separator = "@"
    assert ikidef.first_word(text, separator) == "hello"

    # Test with whitespace as a separator
    text = "hello world"
    separator = " "
    assert ikidef.first_word(text, separator) == "hello"

    # Test with a separator that doesn't exist in the text
    text = "hello.world"
    separator = ","
    assert ikidef.first_word(text, separator) == "hello.world"

#-------------------

def test_current_date_formatting():
    """
    Test scenarios for the `current_date` function to ensure it returns
    the current date in the correct format (DD.MM.YYYY).
    """
    from datetime import datetime

    # Test scenario 1: Verify the format of the returned date
    result = ikidef.current_date()
    expected_format = "%d.%m.%Y"
    try:
        # Attempt to parse the result using the expected format
        parsed_date = datetime.strptime(result, expected_format)
        assert parsed_date.strftime(expected_format) == result
    except ValueError:
        assert False, f"The result '{result}' is not in the expected format '{expected_format}'"

    # Test scenario 2: Verify the returned date matches today's date
    today = datetime.now().strftime("%d.%m.%Y")
    assert result == today, f"Expected today's date '{today}', but got '{result}'"


###################### QUESTIONNAIRE #######################################

def test_is_it_number_valid_inputs():
    """
    Test the is_it_number function with valid numeric inputs, including integers,
    floats, and strings with different decimal separators.
    """
    from src import ikidef

    # Test with integer input
    assert ikidef.is_it_number(42, "Error") == 42.0

    # Test with float input
    assert ikidef.is_it_number(3.14, "Error") == 3.14

    # Test with string input containing a dot as a decimal separator
    assert ikidef.is_it_number("12.34", "Error") == 12.34

    # Test with string input containing a comma as a decimal separator
    assert ikidef.is_it_number("56,78", "Error") == 56.78


def test_is_it_number_invalid_inputs():
    """
    Test the is_it_number function with invalid inputs that cannot be converted to a float.
    """
    from src import ikidef

    # Test with a non-numeric string
    assert ikidef.is_it_number("abc", "Error") == "Error"

    # Test with an empty string
    assert ikidef.is_it_number("", "Error") == "Error"

    # Test with a None value
    assert ikidef.is_it_number(None, "Error") == "Error"

    # Test with a string containing mixed characters
    assert ikidef.is_it_number("12.34abc", "Error") == "Error"


def test_is_it_number_edge_cases():
    """
    Test the is_it_number function with edge case inputs, including very large numbers,
    very small numbers, and unusual formats.
    """
    from src import ikidef

    # Test with a very large number
    assert ikidef.is_it_number("1e10", "Error") == 1e10

    # Test with a very small number
    assert ikidef.is_it_number("1e-10", "Error") == 1e-10

    # Test with a string containing multiple commas
    assert ikidef.is_it_number("1,234,567.89", "Error") == "Error"

    # Test with a string containing multiple dots
    assert ikidef.is_it_number("12.34.56", "Error") == "Error"


#---------------------



def test_true_or_not():
    """
    Test the `true_or_not` function with basic functionality, edge cases, and floating-point precision.
    """
    # Basic functionality
    assert ikidef.true_or_not(10, 5) is True  # 10 >= 5
    assert ikidef.true_or_not(3, 5) is False  # 3 < 5

    # Edge cases
    assert ikidef.true_or_not(5, 5) is True  # 5 == 5
    assert ikidef.true_or_not(-1, 0) is False  # -1 < 0
    assert ikidef.true_or_not(0, -1) is True  # 0 >= -1

    # Floating-point precision
    assert ikidef.true_or_not(0.1, 0.1) is True  # 0.1 == 0.1
    assert ikidef.true_or_not(0.0999999, 0.1) is False  # Slightly less than 0.1
    assert ikidef.true_or_not(0.1000001, 0.1) is True  # Slightly greater than 0.1



#---------------------

def test_consecutive_and_circular_averages_valid_input():
    """
    Test the function with valid inputs.
    """
    # Test with a list of positive numbers
    datalist = [1, 2, 3, 4]
    assert ikidef.consecutive_and_circular_averages(datalist) == [1.5, 2.5, 3.5, 2.5]

    # Test with a tuple of positive numbers
    datalist = (10, 20, 30)
    assert ikidef.consecutive_and_circular_averages(datalist) == [15, 25, 20]

    # Test with a list containing negative numbers
    datalist = [-5, -10, -15]
    assert ikidef.consecutive_and_circular_averages(datalist) == [-7.5, -12.5, -10]

    # Test with a mix of positive and negative numbers
    datalist = [-1, 0, 1]
    assert ikidef.consecutive_and_circular_averages(datalist) == [-0.5, 0.5, 0]

    # Test with a single element repeated
    datalist = [42, 42, 42]
    assert ikidef.consecutive_and_circular_averages(datalist) == [42, 42, 42]


def test_consecutive_and_circular_averages_short_input():
    """
    Test the function with short input (less than 2 elements).
    """
    # Test with an empty list
    assert ikidef.consecutive_and_circular_averages([]) == []

    # Test with a single element
    assert ikidef.consecutive_and_circular_averages([42]) == []


def test_consecutive_and_circular_averages_invalid_input():
    """
    Test the function with invalid inputs.
    """
    # Test with non-numeric elements
    with pytest.raises(TypeError):
        ikidef.consecutive_and_circular_averages([1, "two", 3])

    with pytest.raises(TypeError):
        ikidef.consecutive_and_circular_averages((None, 2, 3))

    # Test with completely invalid types
    with pytest.raises(TypeError):
        ikidef.consecutive_and_circular_averages("123")

    with pytest.raises(TypeError):
        ikidef.consecutive_and_circular_averages(123)

    with pytest.raises(TypeError):
        ikidef.consecutive_and_circular_averages({1, 2, 3})


def test_consecutive_and_circular_averages_edge_cases():
    """
    Test the function with edge cases like zeros and very large numbers.
    """
    # Test with zeros
    datalist = [0, 0, 0]
    assert ikidef.consecutive_and_circular_averages(datalist) == [0, 0, 0]

    # Test with very large numbers
    datalist = [10**6, 10**7, 10**8]
    assert ikidef.consecutive_and_circular_averages(datalist) == [5500000, 55000000, 50500000]



#---------------------

import src.ikidef  

def test_get_sum_avg_min_valid_input():
    """
    Test the function with valid inputs.
    """
    # Test with a list of positive numbers
    data = [1, 2, 3, 4, 5]
    assert src.ikidef.get_sum_avg_min(data) == (15, 3.0, 1)

    # Test with a tuple of positive numbers
    data = (10, 20, 30)
    assert src.ikidef.get_sum_avg_min(data) == (60, 20.0, 10)

    # Test with a list containing negative numbers
    data = [-5, -10, -15]
    assert src.ikidef.get_sum_avg_min(data) == (-30, -10.0, -15)

    # Test with a mix of positive and negative numbers
    data = [-1, 0, 1]
    assert src.ikidef.get_sum_avg_min(data) == (0, 0.0, -1)

    # Test with a single element
    data = [42]
    assert src.ikidef.get_sum_avg_min(data) == (42, 42.0, 42)


def test_get_sum_avg_min_empty_input():
    """
    Test the function with an empty list or tuple.
    """
    with pytest.raises(ValueError, match="Input list or tuple cannot be empty"):
        src.ikidef.get_sum_avg_min([])

    with pytest.raises(ValueError, match="Input list or tuple cannot be empty"):
        src.ikidef.get_sum_avg_min(())


def test_get_sum_avg_min_non_numeric_input():
    """
    Test the function with non-numeric elements in the input.
    """
    with pytest.raises(ValueError, match="All elements in the input must be numeric"):
        src.ikidef.get_sum_avg_min([1, 2, "three"])

    with pytest.raises(ValueError, match="All elements in the input must be numeric"):
        src.ikidef.get_sum_avg_min((1, None, 3))


def test_get_sum_avg_min_invalid_input_type():
    """
    Test the function with invalid input types (not a list or tuple).
    """
    with pytest.raises(ValueError, match="Input must be a list or tuple of numbers"):
        src.ikidef.get_sum_avg_min("123")

    with pytest.raises(ValueError, match="Input must be a list or tuple of numbers"):
        src.ikidef.get_sum_avg_min(123)

    with pytest.raises(ValueError, match="Input must be a list or tuple of numbers"):
        src.ikidef.get_sum_avg_min({1, 2, 3})


def test_get_sum_avg_min_edge_cases():
    """
    Test the function with edge cases like zeros and very large numbers.
    """
    # Test with zeros
    data = [0, 0, 0]
    assert src.ikidef.get_sum_avg_min(data) == (0, 0.0, 0)

    # Test with very large numbers
    data = [10**6, 10**7, 10**8]
    assert src.ikidef.get_sum_avg_min(data) == (111000000, 37000000.0, 1000000)


###################### DRAW #######################################

def test_max_line_length():
    """Test the max_line_length function."""
    text = 'lin1 lin2 lin3 lin4'
    text4 = 'lin1\n\tlin2\n\tlin3\n\tlin4'
    text10 = 'lin1 lin2\n\tlin3 lin4'
    assert drawdef.max_line_length(text, 4) == text4
    assert drawdef.max_line_length(text, 10) == text10  # 'lin1 lin2 ' = 10 characters.
    assert drawdef.max_line_length(text, len(text)) == text




