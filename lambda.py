people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Antonia", "house": "Ravenclaw"},
    {"name": "Adam", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)