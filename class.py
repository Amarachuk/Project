class Flight():
    def  __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
            if not self.open_seats():
                return False
            self.passengers.append(name)
            return True

    def open_seats(self):
            return self.capacity - len(self.passengers)

flight = Flight(250)

people = ["Amara", "Chinemerem", "Uchechi", "Williams", "Jack", "Amelia", "Oliver", "Sophia", "Mason", "Isabella", "Liam", "Mia", "Lucas", "Charlotte", "Ethan", "Harper", "Aiden", "Ava", "Noah", "Chloe", "Benjamin", "Abigail", "Jacob", "Emily", "Michael", "Madison", "Carter", "Elizabeth", "James", "Avery", "Jayden", "Ella", "Logan", "Scarlett", "Ryan", "Grace", "Joseph", "Lily", "Joshua", "Addison", "Andrew", "Natalie", "John", "Zoe", "David", "Lucy", "Christopher", "Bella", "Daniel", "Hannah", "Samuel", "Layla", "Matthew", "Gabriella", "Dylan", "Molly", "Nathan", "Ellie", "Jackson", "Victoria", "Jonathan", "Aubrey", "Wyatt", "Claire", "Tyler", "Riley", "Cameron", "Zoey", "Christian", "Peyton", "Brandon", "Savannah", "Anthony", "Brooklyn", "Josephine", "Landon", "Brianna", "Grayson", "Olivia", "Ian", "Sophie", "Cooper", "Aria", "Gavin", "Stella", "Colton", "Jade", "Nicolas", "Katherine", "Sawyer", "Alexa", "Austin", "Rose", "Eli", "Madelyn", "Jesse", "Faith", "Charlie", "Julia", "Aaron", "Isabelle", "Thomas", "Violet", "Parker", "Alice", "Isaac", "Bailey", "Oliver", "Brielle", "Theodore", "Ruby", "Lincoln", "Lauren", "Leo", "Annabelle", "Julian", "Elise", "Brayden", "Caroline", "Vincent", "Raegan", "Dominic", "Mackenzie", "Edgar", "Leah", "Maverick", "Evelyn", "Josiah", "Angelina", "George", "Nicole", "Adam", "Harley", "Xavier", "Kennedy", "Mateo", "Teagan", "Silas", "Allison", "Jaxon", "Reagan", "Nolan", "Aubree", "Easton", "Camilla", "Damian", "Blake", "Elias", "Maria", "Colin", "Naomi", "Ali", "Luna", "Malachi", "Samantha", "Rhys", "Gianna", "Emerson", "London", "Caden", "Lydia", "Preston", "Elliana", "Kaden", "Kinsley", "Myles", "Marley", "Harrison", "Mya", "Kyle", "Kaitlyn", "Jared", "Amaya", "Joel", "Daisy", "Tristan", "Nevaeh", "Drew", "Serena", "Cayden", "Tessa", "Seth", "Cora", "Ivan", "Paige", "Felix", "Jocelyn", "Jayce", "Marissa", "Griffin", "Lila", "Corbin", "Miranda", "Simon", "Hope", "Marcus", "Kinley", "Zane", "Briana", "Paul", "Chelsea", "Kaleb", "Alaina", "Trenton", "Liliana", "Wesley", "Sienna", "Luka", "Adriana", "Denzel", "Jenna", "Arturo", "Juliette", "Gideon", "Jayla", "Crispin", "Aleah", "Darius", "Josie", "Johan", "Marlee", "Soren", "Donna", "Thaddeus", "Talia", "Raphael", "Journey", "Deacon", "Madilyn", "Abdiel", "Daphne", "Kamari", "Cecilia", "Sonny", "Daniela", "Briggs", "Eden", "Moses", "Fiona", "Otis", "Kayleigh", "Abdullah", "Zara", "Bobby", "Nadia", "Aron", "Ariel", "Marcos", "Jenny", "Jamison", "Esther", "Francis", "Ashlyn", "Hank", "Freya", "Alexis", "Phoebe", "Moises", "Makayla", "Maximus", "Annalise", "Adonis"]

for person in people:
    success = flight.add_passenger(person)
    if success:
                
                print(f"We were able to add {person} to flight successfully")
    else:
                
                print(f"No flights are available for {person}")
  