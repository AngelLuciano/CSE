states = {
    "CA": "California",
    "NJ": "New Jersey",
    "WI": "Wisconsin",
    "NY": "New York"
}

print(states["CA"])
print(states["WI"])

complex_dictionary = {"CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "NJ": {
        "NAME": "New Jersey",
        "POPULATION": 9000000,
        "CITIES": [
            "Newark",
            "Trenton",
            "Princeton"
        ]
    },
    "WI": {
        "NAME": "WISCONSIN",
        "POPULATION": 5800000,
        "CITIES": [
            "Madison",
            "Milwaukee",
            "Green Bay"
        ]
    },
    "NY": {
        "NAME": "NEW YORK",
        "POPULATION": 19500000,
        "CITIES": [
            "New York City",
            "Rockester",
            "Buffalo"
        ]
    }
}

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000
    },
    "NJ": {
        "NAME": "New Jersey",
        "POPULATION": 9000000
    },
    "WI": {
        "NAME": "WISCONSIN",
        "POPULATION": 5800000
    },
    "NY": {
        "NAME": "NEW YORK",
        "POPULATION": 19500000
    }
}
print(nested_dictionary["CA"])
print(nested_dictionary["CA"]["POPULATION"])
print(nested_dictionary["NY"])
print(nested_dictionary["NY"]["NAME"])
print(complex_dictionary["NY"]["CITIES"][0])
print(complex_dictionary["NJ"]["CITIES"][2])

print(complex_dictionary.keys())
print(complex_dictionary.items())
print(nested_dictionary.items())

for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)

print()
for state, info in complex_dictionary.items():
    for title, desc in info.items():
        print(title)
        print(desc)
        print("-" * 20)
    print("-" * 20)

states["MN"] = "Mississippi?"

states["MN"] = "Minnesota"
