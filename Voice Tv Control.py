class VoiceCommand:

    def __init__(self, channels):
        self.channels = channels
        self.channel = 0

    def first_channel(self):
        self.channel = 0
        return self.channels[0]

    def last_channel(self):
        self.channel = len(self.channels) - 1
        return self.channels[-1]

    def turn_channel(self, number):
        self.channel = number - 1
        return self.channels[self.channel]

    def next_channel(self):
        if self.channel != len(self.channels) - 1:
            self.channel += 1
        else:
            self.channel = 0
        return self.channels[self.channel]

    def previous_channel(self):
        if self.channel:
            self.channel -= 1
        else:
            self.channel = len(self.channels) - 1
        return self.channels[self.channel]

    def current_channel(self):
        return self.channels[self.channel]

    def is_exist(self, sample):
        if sample in (self.channels + list(range(len(self.channels)))):
            return 'Yes'
        return 'No'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")
