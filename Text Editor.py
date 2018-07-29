class Text:

    def __init__(self):
        self.text, self.font = '', ''

    def write(self, text):
        self.text += text

    def set_font(self, font):
        self.font = font

    def show(self):
        if self.font:
            return '[{0}]{1}[{0}]'.format(self.font, self.text)
        return self.text

    def restore(self, old_text):
        self.text, self.font = old_text[0], old_text[1]


class SavedText:

    def __init__(self):
        self.ver, self.saved_text = 0, []

    def save_text(self, new_text):
        self.saved_text += [[new_text.text, new_text.font]]
        self.ver += 1

    def get_version(self, number):
        return self.saved_text[number]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
