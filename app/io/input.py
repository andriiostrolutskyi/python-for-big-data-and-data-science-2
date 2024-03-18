def text_input():
    """
    Function to receive text input from the console.

    Returns:
        str: The text inputted by the user.
    """
    user_input = input("Enter text: ")
    return user_input


def read_from_file(filename):
    """
    Function to read from a file using built-in Python capabilities.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        str: Content read from the file.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."


def read_with_pandas(filename):
    """
    Function to read from a file using the pandas library.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        pandas.DataFrame: DataFrame containing the data read from the file.
    """
    try:
        import pandas as pd
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        return "File not found."
