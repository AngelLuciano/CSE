

# option 2
R19A = Room("Mr. Weibe's Room", 'parking_lot')
parking_lot = Room("The Parking Lot", None, 'R19A', 'Market')
Market = Room("Zack's Market", 'parking_lot')
Teleporter = Room("Teleporter", 'Market')
Store = Room("Family dollar"'parking_lot')
 = Room("")


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

