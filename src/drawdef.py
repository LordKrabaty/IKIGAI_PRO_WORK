"""Function module for ikidraw."""

def max_line_length(text: str, max_length: int) -> str:
    """Divides text into multiple lines if the current lines exceed the specified maximum length.

    Args:
        text (str): The input text to be processed.
        max_length (int): The maximum allowed length for each line.

    Returns:
        str: The modified text with lines adjusted to the specified maximum length.
    """
    text_mod = ""  # Empty string for storing the modified text.
    line_separator = '\n'  # Character used to separate lines.
    word_separator = ' '  # Character used to separate words.

    for line in text.split(line_separator):
        current_line = ''  # Temporary variable for building the current line.
        words = line.split(word_separator)  # Splits the line into words.

        for word in words:
            line_length = len(current_line)  # Current line's length.
            word_length = len(word)  # Length of the current word.
            word_separator_length = len(word_separator)  # Length of the separator.

            # Add the word to the current line if it does not exceed the maximum length.
            if line_length + word_separator_length + word_length <= max_length:
                if current_line:  # Add separator if the current line is not empty.
                    current_line += word_separator
                current_line += word  # Append the word to the current line.
            else:
                # Add the current line to the modified text and start a new line.
                text_mod += line_separator + current_line
                current_line = '\t' + word  # Start a new line with a tab for better readability.

        if current_line:  # Add the last line if it exists.
            text_mod += line_separator + current_line

    text = text_mod.strip()  # Remove leading/trailing separators.
    return text


def color_by_limits(value_ask: float, value_max: float, value_min_true: float):
    """Sets the turtle's color based on the given value's position relative to limits.

    Args:
        value_ask (float): The value to evaluate.
        value_max (float): The maximum limit.
        value_min_true (float): The minimum acceptable limit.

    Returns:
        turtle.color: The color corresponding to the value's range.
    """
    from turtle import color

    if value_ask == value_max:
        return color('green')  # Maximum value is green.
    elif value_ask >= value_min_true:
        return color('dark goldenrod')  # Within acceptable range is dark goldenrod.
    else:
        return color('red')  # Below minimum limit is red.
