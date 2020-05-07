import html


def cleanse_input(input_string):
    """
    This function will take an input string and perform cleansing functions on it.  This will help ensure that injection
    attacks are prevented
    :param input_string: The string as given by the http request
    :return input_string:  Ths string after all cleansing functions are done on it.
    """
    if input_string is None:
        input_string = ""
    input_string = input_string.strip()
    input_string = html.escape(input_string)
    return input_string
