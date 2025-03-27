"""Function module for the main module."""

# USER DATA -----------------------------------------------------------------------------------

def input_limit(question: str, min_length: int, max_length: int) -> str:
    """Gets user input with a defined minimum and maximum number of characters.
    
    A while loop is used to validate the input, with printed instructions for the user.

    Args:
        question (str): The question to prompt the user.
        min_length (int): The minimum number of characters allowed.
        max_length (int): The maximum number of characters allowed.

    Returns:
        str: The validated user input.
    """
    question = question + ' '  # Add a space after the question for better formatting.
    user_input = input(question)
    length_input = len(user_input)

    while length_input < min_length or length_input > max_length:
        msg_length = (
            f"Your input must be between {min_length} and {max_length} characters long. "
            f"Your answer '{user_input}' is not. Try again."
        )
        print(msg_length)
        user_input = input(question)
        length_input = len(user_input)
    
    return user_input


def first_word(text: str, separator: str) -> str:
    """Extracts the first word from the text before the first occurrence of the separator.

    Args:
        text (str): The input text.
        separator (str): The character or string used as a separator.

    Returns:
        str: The first word before the separator.
    """
    if separator in text:
        space_name = text.index(separator)
        return text[:space_name]
    else:
        return text


def current_date() -> str:
    """Gets the current date in the format DD.MM.YYYY.

    Returns:
        str: The current date formatted as DD.MM.YYYY.
    """
    from datetime import datetime
    current_date = datetime.now()  # Get the current date and time.
    return current_date.strftime("%d.%m.%Y")  # Format the date as DD.MM.YYYY.


###################### QUESTIONNAIRE #######################################

# FIRST SET OF QUESTIONS ---------------------------------------------------------------------------------------------

def is_it_number(value, msg_value: str):
    """Checks if a value can be converted to a float. 
    If not, returns a specified error message. Supports both '.' and ',' as decimal separators.

    Args:
        value: The value to check.
        msg_value (str): The error message to return if the value is not a number.

    Returns:
        float or str: The float representation of the value if valid, otherwise the error message.
    """
    value = str(value)
    value = value.replace(',', '.')  # Replace ',' with '.' to handle different decimal separators.

    try:
        return float(value)
    except ValueError:
        return msg_value


def ask_for_number(question: str, value_min: float, value_max: float) -> float:
    """Prompts the user for a number within a specified range and returns the input as a float.

    Args:
        question (str): The question to prompt the user.
        value_min (float): The minimum allowable value.
        value_max (float): The maximum allowable value.

    Returns:
        float: The validated number input from the user.
    """
    while True:
        question = f'Answer within the range {value_min}-{value_max}: {question} '
        value = input(question)
        msg_value = f"You must enter a number. '{value}' is not a number! Try again."
        value = is_it_number(value, msg_value)

        if value == msg_value:
            print(msg_value)
        else:
            if value_min <= value <= value_max:  # Check if the value is within the range.
                return value
            
            msg_limit = f"Your answer '{value}' is out of range! Try again."
            print(msg_limit)  # Notify the user if the value is out of range.


def true_or_not(value: float, min_true: float) -> bool:
    """Determines if the value is greater than or equal to a specified minimum threshold.

    Args:
        value (float): The value to evaluate.
        min_true (float): The minimum threshold.

    Returns:
        bool: True if the value is >= min_true, otherwise False.
    """
    return value >= min_true


def ask_for_yn(yn_question: str, positive: str, negative: str, msg_error: str) -> bool:
    """Prompts the user for a yes/no answer and returns True or False based on the response.

    Args:
        yn_question (str): The question to prompt the user.
        positive (str): The string representing a positive response.
        negative (str): The string representing a negative response.
        msg_error (str): The error message to display for invalid input.

    Returns:
        bool: True for a positive response, False for a negative response.
    """
    while True:
        yn_question = yn_question + ' '  # Add a space after the question for better formatting.
        answer = input(yn_question)

        if answer == positive:
            return True
        if answer == negative:
            return False
        
        print(msg_error)
