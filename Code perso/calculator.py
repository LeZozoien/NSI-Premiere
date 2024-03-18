def get_char_type(char:str):
    """ 
    Returns a string denoting the type of char. 

    >>> get_char_type('x')
    'letter'
    """
    operators = {'*', '/', '+', '-', '=', '%', '~', '/', '&', '|', '>', '<'}
    if char.isdigit():
        char_type = 'number'
    elif char.isalpha():
        char_type = 'letter'
    elif char in operators:
        char_type = 'operator'
    else:
        char_type = 'other'
    return char_type

def tokenize(string):
    """
    Generates tokens from a mathematical statement string.

    >>> list(tokenize('3 + (4 ∗ 5)'))
    ['3', '+', '(', '4', '∗', '5', ')']

    >>> list(tokenize('x+=10'))
    ['x', '+=', '10']

    >>> list(tokenize('(729 + 4 * variable) ** 22 // 3'))
    ['(', '729', '+', '4', '*', 'variable', ')', '**', '22', '//', '3']
    """
    token_type = get_char_type(string[0])
    token = ''
    for char in string:
        if char == ' ':
            continue  # Spaces are not included
        new_type = get_char_type(char)
        if new_type != token_type:  # A new type of token has been found 
            yield token
            token_type = new_type
            token = ''
        token += char
    if len(token) > 0:
        return token


print(list(tokenize("0 + 6+ 3-8 * 0")))