class Country:
    def __init__(self, country):
        self.country = country

class State(Country):
    def __init__(self, country, state):
        super().__init__(country)
        self.state = state

class City(State):
    def __init__(self, country, state, city):
        super().__init__(country, state)
        self.city = city

    def display(self):
        print("Country :", self.country)
        print("State :", self.state)
        print("City :", self.city)

c = City("India", "Gujarat", "Ahmedabad")
c.display()


    

