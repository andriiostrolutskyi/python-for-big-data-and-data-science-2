def output_to_console(text):
    """
    Function to output text to the console.

    Args:
        text (str): Text to be printed to the console.

    Returns:
        None
    """
    print(text)


def write_to_file(text, filename):
    """
    Function to write to a file using built-in Python capabilities.

    Args:
        text (str): Text to write to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        file.write(text)

