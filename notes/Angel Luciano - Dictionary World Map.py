name = 'NAME'
world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's room",
        'DESCRIPTION': "This is the room that you are in.",
        'PATHS': {
            'NORTH': "PARKING_LOT",
            'DOWN': "TELEPORTER"
        }
    },
    'PARKING_LOT': {
        'NAME': "A Parking Lot",
        'DESCRIPTION': "There are a few cars parked here.",
        'PATHS': {
            'SOUTH': 'R19A',
            'WEST': 'STORE',
            'EAST': "MARKET"
        }
    },
    'HOUSE': {
        'NAME': "A House",
        'DESCRIPTION': "Looks like no one live here",
        'PATHS': {
            'EAST': "STORE",
            'NORTH': "HOUSE1"
        }
    },
    "MARKET": {
        'NAME': "Zack's Market",
        'DESCRIPTIONS': "This is the market that everyone loves to go to",
        'PATHS': {
            'WEST': "PARKING_LOT"
        }
    },
    "TELEPORTER": {
        'NAME': "Underground teleporter",
        'DESCRIPTIONS': "Wonder who's is this",
        'PATHS': {
            'UP': "R19A"
        }
    },
    "STORE": {
        'NAME': "FAMILY DOLLAR",
        'DESCRIPTION': "Never knew a store was that close",
        'PATHS': {
            'WEST': "HOUSE",
            'EAST': "PARKING_LOT"
        }
    },
    "HOUSE1": {
        'NAME': "LIVING ROOM",
        'DESCRIPTION': "ABOUT TIME I BROKE IN",
        'PATHS': {
            'NORTH': "BACKYARD",
            'SOUTH': "HOUSE"
        }
    },
}

descriptions = {'d', "d", "Descriptions", "description"}
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
current_node = world_map["R19A"]
playing = True

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])

    command = input("Where would you like to go")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node['PATHS'][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized")
