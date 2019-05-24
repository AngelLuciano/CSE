class Item(object):
    def __init__(self, name):
        self.name = name


class Vehicle(Item):
    def __init__(self, name):
        super(Vehicle, self).__init__(name)


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Key(object):
    def __init__(self, name):
        self.name = name
        self.door = True

    def open_door(self):
        R19A.down = 'teleporter'


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)


class Walkietalkie(Item):
    def __init_(self, name):
        self.name = name


class Jetpack(Item):
    def __init_(self, name, fly):
        self.name = name
        self.name = fly
        self.fly = True
        self.flying = 10

    def flying(self):
        if self.fly:
            if self.flying < 10:
                print("You need one more part for your wings")

            else:
                print("Your are now in the air")


class Wraith(Vehicle):
    def __init_(self, gas, miles):
        super(Wraith, self).__init__(Vehicle)
        if gas < 1:
            print("You are speeding off in the foreign")
        else:
            print("Where are the keys at")
        if miles < 2:
            print("We need to get a oil check")


class Character(object):
    def __init__(self, name, health, weapon, armor, armor_type):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.armor_type = armor_type

    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No Damage is done because of your armor!")
        else:
            self.health -= damage - self.armor.armor_amt
            if self.health < 0:
                self.health = 0
                print("% has fallen" % self.name)
            print("%s has %d damage" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


sword = Weapon("Sword", 10)
canoe = Weapon("Canoe", 84)
weibe_armor = Armor("Armor of the gods", 100000000000)

orc = Character("orc", 100, Weapon(sword, 100), Armor, "Generic Armor")
weibe = Character("weibe",  100000, Weapon(sword, 100000), Armor, "Armor of the gods")


def pick_up(self, grab):
    self.grab
    if grab > 1:
        grab


class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, down=None, up=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.up = up
        self.description = "ENTER DESCRIPTION HERE"

# option 2


R19A = Room("Mr. Weibe's Room", 'parking_lot', None, None, None, 'Teleporter', None,)
parking_lot = Room("The Parking Lot", None, 'R19A', 'Market', 'Store', None, None)
Market = Room("Zack's Market", None, None, None, 'parking_lot', None, None)
Teleporter = Room("Teleporter", None, None, None, None, None, 'R19A')
Store = Room("Family dollar", 'House', 'Parking_lot', None)
House = Room("House", 'House1', None, 'Store')
House1 = Room("Living room", None, 'House', None)
Backyard = Room("Backyard", None, 'House1', 'Public_library', 'Tennis_courts', None)
Tennis_courts = Room("Tennis courts", None, None, 'Backyard')
Public_library = Room("Public Library", 'Park', 'Apartments', None, 'Backyard')
Park = Room("Park", None, 'Public_library' 'Public_pool', None)
Public_pool = Room("Public pool", None, 'Video_game_store', None, 'Park', None)
Video_game_store = Room("Video Game Store", 'Public_pool', 'Zoo', 'Escape_room', None)
Escape_room = Room("Escape room", None, None, None, 'Escape_room', None)
Zoo = Room("Fresno chaffee zoo", 'Video_game_store', None)


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """

        :param new_location:
        """
        self.current_location = new_location

    def find_room(self, direction):
        """

        :param direction: A string (all lowercase), with a cardinal direction
        :return: a room object if it exist, None if it does not
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]


player = Player(R19A)
directions = ('north', 'south', 'east', 'west', 'up', 'down')
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
pick_up = ["Pick up"]
playing = True

command = input(">_")


while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input("<_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized")
    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    elif "take" in command.lower():
