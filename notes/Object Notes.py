class Laptop(object):
    def __init__(self, screen_resolution, extra_space=1000, color="Cobalt"):
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = color
        self.os = "Linux"
        self.functioning = True

    def charge(self, time):
        if self.functioning:
            if self.battery_left >= 100:
                print("The computer is already charged.")
                return

            self.battery_left += time

            if self.battery_left > 100:
                print("The computer quickly charges.")
                self.battery_left = 100

            else:
                print("The computer is now at %d%%." % self.battery_left)
        else:
            print("It's broken good job")

    def smash(self):
        self.functioning = False
        print("I took the laptop. . .")
        print()
        print()
        print()
        print(". . .AND I THREW IT ON the ground!!!!!")

    def use(self, time):
        self.battery_left -= time
        print("You use the laptop for  %s minutes" % time)


my_computer = Laptop("1920x1080", 10000, "Black")
your_computer = Laptop("10x10", 0, "Orange")
weibe_computer = Laptop("9000000000x900000000", 9000000000000000, "Awesome")
default_computer = Laptop("1920x1080")

my_computer.use(60)
my_computer.charge(20)
my_computer.charge(1000)
my_computer.smash()
my_computer.charge(20)

your_computer.charge(20)
