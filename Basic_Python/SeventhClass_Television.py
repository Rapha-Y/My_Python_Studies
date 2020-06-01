class Television:

    def __init__(self):
        self.on = False
        self.channel = 5

    def power(self):
        self.on = not self.on

    def channel_up(self):
        if self.on:
            self.channel += 1

    def channel_down(self):
        if self.on:
            self.channel -= 1

print(__name__)
if __name__ == '__main__':

    television = Television()
    print(television.on)

    television.power()
    print(television.on)

    television.power()
    print(television.on)

    television.power()
    print(television.channel)

    television.channel_up()
    television.channel_up()
    print(television.channel)

    television.channel_down()
    print(television.channel)