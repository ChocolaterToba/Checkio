import string


def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


LETTERS_NUMBERS = list(map(convert,
                           [1, 3, 9, 25, 17, 11, 27, 19, 10, 26,
                            5, 7, 13, 29, 21, 15, 31, 23, 14, 30,
                            37, 39, 62, 45, 61, 53, 47, 63, 55, 46, 26]))
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {",": convert(2), "-": convert(18), "?": convert(38),
               "!": convert(22), ".": convert(50), "_": convert(36)}
WHITESPACE = convert(0)
BOOK = list(string.ascii_lowercase)
def make_page(braille):
    result = [[], [], []]
    for i in range(3):
        for letter in braille:
            result[i] += [letter[i][0], letter[i][1], 0]
        x = result[i].pop(-1)
    return result


def braille_page(text: str):
    result = []
    for symbol in list(text):
        if symbol.isalpha():
            if symbol not in BOOK:
                result += [CAPITAL_FORMAT]
                symbol = symbol.lower()
            result += [LETTERS_NUMBERS[BOOK.index(symbol)]]
        elif symbol.isdigit():
            result += [NUMBER_FORMAT]
            if symbol == '0':
                result += [LETTERS_NUMBERS[9]]
            else:
                result += [LETTERS_NUMBERS[int(symbol) - 1]]
        elif symbol in PUNCTUATION:
            result += [PUNCTUATION[symbol]]
        else:
            result += [WHITESPACE]
    if len(result) < 11:
        return make_page(result)
    while len(result) % 10 != 0:
        result += [WHITESPACE]
    result1 = []
    while result:
        result1 += make_page([result[k] for k in range(10)])
        result1 += [[0 for a in range(29)]]
        result = result[10:]
    return result1[:-1]

print(braille_page("hello 1st World!"))
            
