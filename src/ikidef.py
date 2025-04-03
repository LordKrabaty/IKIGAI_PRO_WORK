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


def get_sum_avg_min(data: list | tuple) -> tuple[float, float, float]:
    """
    Calculates the sum, average, and minimum value from a list or tuple of numbers.

    Args:
        data (list | tuple): A list or tuple containing numeric values.

    Returns:
        tuple[float, float, float]: A tuple containing the sum, average, and minimum value.

    Raises:
        ValueError: If the input is not a list or tuple, or if it contains non-numeric elements.
        ValueError: If the input list or tuple is empty.
    """
    from statistics import mean

    # Validate that the input is either a list or tuple
    if not isinstance(data, (list, tuple)):
        raise ValueError("Input must be a list or tuple of numbers.")

    # Ensure the input is not empty
    if not data:
        raise ValueError("Input list or tuple cannot be empty.")

    # Verify that all elements in the input are numeric
    if not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("All elements in the input must be numeric.")

    # Perform calculations: sum, average, and minimum
    data_sum = sum(data)
    data_avr = mean(data)  
    data_min = min(data)  

    return data_sum, data_avr, data_min

def consecutive_and_circular_averages(datalist: list| tuple) -> list:
    """
    Calculates the averages between every two consecutive elements in a tuple.

    Args:
        datalist (list or tuple): Input tuple containing any number of numeric elements.

    Returns:
        list: A list of averages between consecutive elements.
    """
    from statistics import mean

    # Return an empty list if the tuple is too short to calculate averages
    if len(datalist) < 2:
        return []

    # Initialize an empty list to store the averages
    averages = []

    # Iterate through the tuple to calculate averages of consecutive elements
    for i in range(len(datalist) - 1):
        # Take two consecutive elements
        first_element = datalist[i]
        second_element = datalist[i + 1]

        # Calculate their average and append the result to the averages list
        average = mean((first_element, second_element))
        averages.append(average)

    # Calculate the circular average (last element + first element) + append
    last_element = datalist[-1]
    first_element = datalist[0]
    circular_average = mean((last_element, first_element))
    averages.append(circular_average)

    return averages




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
