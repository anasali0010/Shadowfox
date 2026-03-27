class Avenger:
    def __init__(self, name, age, gender, power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.power = power
        self.weapon = weapon
        self.leader = leader

    # Method to display info
    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Power: {self.power}")
        print(f"Weapon: {self.weapon}")
        

    # Method to check leader
    def is_leader(self):
        return f"{self.name} is a Leader" if self.leader else f"{self.name} is not a Leader"


# Creating Avengers
av1 = Avenger("Captain America", 100, "Male", "Super Strength", "Shield", True)
av2 = Avenger("Iron Man", 48, "Male", "Technology", "Armor")
av3 = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
av4 = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
av5 = Avenger("Thor", 1500, "Male", "Super Energy", "Mjolnir")
av6 = Avenger("Hawkeye", 38, "Male", "Fighting Skills", "Bow and Arrows")

# Display Info
avengers = [av1, av2, av3, av4, av5, av6]

for av in avengers:
    av.get_info()
    print(av.is_leader())
    print("-" * 20)