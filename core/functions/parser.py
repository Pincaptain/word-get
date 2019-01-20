
def is_valid_query(query):

    """
    Validates the query passed as a parameter.
    Returns true if the query is valid and false if it isn't.

    :param query:
    :return bool:
    """

    if query is None:
        return False

    if len(query) == 0:
        return False

    return True


def get_word_desc(text):

    """
    To be used explicitly for extracting the description from a word.
    Used during scraping.
    Filters the string from the last to the first brace reversing it at the end.

    :param text:
    :return string:
    """

    # Resulting description
    desc = ''
    # Multiple brace escape stack
    stack = ['.']
    # Reverse text for iteration
    reverse = text[::-1].strip()

    # Iterates over each character in the text
    for char in reverse:
        # If it reaches a closed brace adds it to the stack
        if char == ')':
            if '.' in stack:
                stack.pop()

            stack.append(')')

        # If it reaches an open brace pops a brace from the stack
        if char == '(':
            stack.pop()

        # Otherwise adds the character to the description
        if '.' not in stack:
            desc += char

        # If the stack is empty breaks
        if len(stack) == 0:
            break

    # Bring the string to his original state
    desc = desc[::-1]
    # Remove the first and the last brace
    desc = desc[1: len(desc) - 1]

    # Return a capitalized version of the string
    return desc.capitalize()


def get_word_examples(text):

    """
    To be used explicitly for extracting the examples from a word.
    Used during scraping.
    Filters the string from the end to the start searching for examples.

    :param text:
    :return string:
    """

    # Resulting examples list
    examples = []
    # Multiple quotes escape stack
    stack = []
    # Reverse text for iteration
    reverse = text[::-1].strip()
    # Represents a single example
    example = ''

    # Iterates over every character in the text
    for char in reverse:
        # If char is closed brace break
        if char == ')':
            break

        # If char is quotes but no quotes in stack add them to stack
        if char == '"' and len(stack) == 0:
            stack.append(char)

        # Add the character to the example string
        example += char

        # If char is quotes but there is already quotes inside the stack
        if char == '"' and len(stack) != 0:
            stack.pop()

            example = example[::-1].strip()
            example = example[1: len(example)]
            example = example.capitalize()

            examples.append(example)

            example = ''

    # Clear all empty strings
    for example in examples:
        if example == '' or example == ';':
            examples.remove(example)

    return examples
