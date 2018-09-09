class MicrowaveBase:
    def show_time(self, minutes, seconds):
        pass


class Microwave1(MicrowaveBase):
    def show_time(self, minutes, seconds):
        return '_{}:{}'.format(minutes[1], seconds)


class Microwave2(MicrowaveBase):
    def show_time(self, minutes, seconds):
        return '{}:{}_'.format(minutes, seconds[0])


class Microwave3(MicrowaveBase):
    def show_time(self, minutes, seconds):
        return '{}:{}'.format(minutes, seconds)


class RemoteControl:
    def __init__(self, microvawe):
        self.microvawe = microvawe
        self.total_time = 0

    def set_time(self, time):
        self.total_time = int(time[:2]) * 60 + int(time[3:])

    def add_time(self, add):
        if add[-1] == 's':
            self.total_time += int(add[:-1])
        else:
            self.total_time += 60 * int(add[:-1])
        if self.total_time > 5400:
            self.total_time = 5400

    def del_time(self, sub):
        if sub[-1] == 's':
            self.total_time -= int(sub[:-1])
        else:
            self.total_time -= 60 * int(sub[:-1])
        if self.total_time < 0:
            self.total_time = 0

    def show_time(self):
        self.minutes = str(self.total_time // 60).zfill(2)
        self.seconds = str(self.total_time % 60).zfill(2)
        return self.microvawe.show_time(self.minutes, self.seconds)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")
