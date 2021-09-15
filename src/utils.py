import re

def to_snake_case(name):
    '''
    Converts a Pascal case string to snake case
    INPUT
    name - a string to be converted to snake case
    OUTPUT
    name - the string converted to snake case
    '''
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('__([A-Z])', r'_\1', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower()