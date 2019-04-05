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
        self.key = 1

    def open_door(self):
        if self.door:
            if


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)


class Walkietalkie(Item):
    def __init_(self, name):
        self.name = name
        if  name = 1:
            




class Jetpack(Item):
    def __init_(self, name, fly):
        self.name = name
        self.name = fly
        self.fly = True
        self.flying = 10

    def flying(self):
        if self.fly:
            if self.flying < 10 :
                print("You need one more part for your wings")

            else:
                print("Your are now in the air")


class wingsuit(Item):
    def __init_(self, name):
        self.name = name

    def gliding(self):
        if self.glide:
            if self.gliding < 11 :
                 if gliding is  -= 4




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
    def __init_(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def pick_up(self, grab ):
        if grab > 1 :
            grab

        

    def take_damage(self, damage):
        self.health -= damage - self.armor.armor_amt
        if damage < self.armor.armor_amt:
            print("No Damage is done because of your armor!")
        else:
            self.health -= damage - self.armor.armor_amt
            print(self.fallen) % self.name)
        print("%s has %d damage" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


Sword = Weapon("Sword", 10)
canoe = Weapon("Canoe", 84)
wiebe_armor = Armor("Armor of the gods", 100000000000)

orc = Character ("orc"), 10, Sword, Armor("Dark Wing")
wiebe = Character ("wiebe"), 200, Sword, Armor("Armor of the gods")

orc.attack(Wiebe)
wiebe.attack(orc)

class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = "ENTER DESCRIPTION HERE"


R19A = Room("Mr. Weibe's Room")
parking_lot = Room("The Parking Lot", None, R19A)

R19A.north = parking_lot

# option 2
R19A = Room("Mr. Weibe's Room", 'parking_lot')
parking_lot = Room("The Parking Lot", None, 'R19A', 'Market')
Market = Room("Zack's Market", 'parking_lot')
Teleporter = Room("Teleporter", 'Market')
Store = Room("Family dollar"'parking_lot')
Pool = Room("")


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
playing = True

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

