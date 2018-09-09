from re import findall, split, match
from itertools import chain, zip_longest


class HackerLanguage:
    def __init__(self):
        self.text = ''

    def write(self, new_text):
        self.text += new_text

    def delete(self, N):
        self.text = self.text[:-N]

    def send(self):
        # dates_first shows whether we should put new_text's elements first
        # while 'joining' dates_first and new_text.
        dates_first = match(r'\d{2}\.\d{2}\.\d{4}|\d{2}:\d{2}', self.text)
        # Getting dates, times, special symbols out of the text.
        dates_times = findall(r'\d{2}\.\d{2}\.\d{4}|\d{2}:\d{2}|[!?$%@.:]',
                              self.text)
        # Getting text cleared from dates, times, special symbols.
        new_text = split(r'\d{2}\.\d{2}\.\d{4}|\d{2}:\d{2}|[!?$%@.:]',
                         self.text)
        # Converting each symbol into binary.
        for a, text in enumerate(new_text):
            formatted_text = ''
            for i in text:
                if i == ' ':
                    i = '1000000'
                else:
                    i = bin(ord(i))[2:]
                formatted_text += i
            new_text[a] = formatted_text
        # 'Joining' two lists together.
        if dates_first:
            return ''.join(list(chain(*zip_longest(dates_times, new_text,
                                                   fillvalue=''))))
        else:
            return ''.join(list(chain(*zip_longest(new_text, dates_times,
                                                   fillvalue=''))))

    def read(self, text):
        ''' Same as send(), but we get characters from binary. '''
        dates_first = match(r'\d{2}\.\d{2}\.\d{4}|\d{2}:\d{2}', text)
        dates_times = findall(r'\d{2}\.\d{2}\.\d{4}|\d{2}:\d{2}|[!?$%@.:]',
                              text)
        new_text = split(r'\d{2}\.\d{2}\.\d{4}|\d{2}:\d{2}|[!?$%@.:]', text)
        for a, item in enumerate(new_text):
            formatted_text = ''
            for b in range(int(len(item) / 7)):
                i = item[:7]
                if i != '1000000':
                    formatted_text += chr(int(i, 2))
                else:
                    formatted_text += ' '
                item = item[7:]
            new_text[a] = formatted_text
        if dates_first:
            return ''.join(list(chain(*zip_longest(dates_times, new_text,
                                                   fillvalue=''))))
        else:
            return ''.join(list(chain(*zip_longest(new_text, dates_times,
                                                   fillvalue=''))))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
