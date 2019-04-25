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

class Chestplate(Armor):
    def __init__(self):



class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage

class Sword(Weapon):
    def __init_subclass__(cls, **kwargs):


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


class Wing_suit(Item):
    def __init_(self, name):
        self.name = name


class Wraith(Vehicle):
    def __init_(self):
        super(Wraith, self).__init__(Vehicle)
        if gas < 1:

class Phone(Item)
    def __init__(self):

class Crossbow(Weapon):
    def __init__(self):c  ,,vllvcm;lv;ldmvmcl;vmlfdml;lfdmld;mf;ldsml;cdml;dfml;smfdl;dmf;lfm;ldm;lfdm;lfmv,mv,.vmdfldfl;kds;lskl;fl;kfl;kdsfm,l;.lKKKjfgjkffdlkjlkjkjfkjksfdjkdnvcdsjierjfikdjfjseifjdkla;we

class Buggati(Vehicle):
    def __init__(self):

class Boat(Vehicle)
    def __init__(self):

class Bat(Weapon):
    def __init__(self):

class Book(Item):
    def __init__(self):

class Helmet(Armor):
    def __init__(self):

class Skateboard(Vehicle)
    def __init__(self):





class Character(object):
    def __init_(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage - self.armor.armor_amt
        if damage < self.armor.armor_amt:
            print("No Damage is done because of your armor!")
        else:
            self.health -= damage - self.armor.armor_amt
        if self.health < 0:
            self.health = 0
            print("%s has fallen" % self.name)
        print("%s has %d damage" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


Sword = Weapon("Sword", 10)
canoe = Weapon("Canoe", 84)
wiebe_armor = Armor("Armor of the gods", 100000000000)

orc = Character("orc"), 10, Sword, Armor("Dark Wing")
wiebe = Character("wiebe"), 200, Sword, Armor("Armor of the gods")

orc.attack(Wiebe)
wiebe.attack(orc)