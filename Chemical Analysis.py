from re import findall, split


def open_brackets(string):
    '''Yield modified('opened') string.'''
    # Getting the multiplier if there is one after brackets.
    for i in range(len(string)):
        if string[i] in [']', ')']:
            mul = int(string[i + 1:])
            string = string[:i + 1]
            break
    else:
        mul = 1
    # Removing brackets.
    string = string[1:-1]
    # Multiplying elements' quantities by mul.
    for elem in findall(r'[A-Z][a-z]?\d*', string):
        elem_len = 1
        if len(elem) > elem_len:
            if elem[1].islower():
                elem_len = 2
        if len(elem) == elem_len:
            yield elem + str(mul)
        else:
            yield elem[:elem_len] + str(int(elem[elem_len:]) * mul)


def modify_formula(formula):
    '''Yield modified versions of all strings with brackets.'''
    for string in findall(r'(?:\(\w+\)|\[\w+\])\d*', formula):
        yield ''.join(list(open_brackets(string)))

def atoms(formula, limit):
    '''Find all elements from formula with quantity >= limit.'''
    elements = dict()
    # Opening all brackets in formula
    while '(' in formula or '[' in formula:
        new_formula = split(r'(?:\(\w+\)|\[\w+\])\d*', formula)
        for i, string in enumerate(modify_formula(formula)):
            if formula[0] in ['(', '[']:
                new_formula[i] = string + new_formula[i]
            else:
                new_formula[i] += string
        formula = ''.join(new_formula)
    # Counting each element's quantities.
    for elem in findall(r'[A-Z][a-z]?\d*', formula):
        if not elem[-1].isdigit():
            elem += '1'
        elem_len = 1
        # This is a bugfix in case the element is 2-lettered, like 'Mg'.
        if elem[1].islower():
            elem_len = 2
        if elem[:elem_len] in elements:
            elements[elem[:elem_len]] += int(elem[elem_len:])
        else:
            elements[elem[:elem_len]] = int(elem[elem_len:])
    return list(key for key in elements if elements[key] >= limit)
print(atoms('K4[O3N(SO)2]2', 4))
            
                
