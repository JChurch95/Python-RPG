# Create class Character that the classes of Hero and Goblin will pull from
class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

# If the character's health is greater than 0, it will return True to being alive.
    def alive(self):
        return self.health > 0
    
# Whenever a character (which is assigned to Hero and Goblin) attacks an enemy, it will print who attacked who and then give back a value of the enemies health
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.__class__.__name__} attacked {enemy.__class__.__name__}!")
        print(f"{enemy.__class__.__name__}'s health is now {enemy.health}")



# Classes of Hero and Goblin
class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health, power)

    
    
    def print_status(self):
        print (f"You have {self.health} health and {self.power} power.")



class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
    

    
    def print_status(self):
        print (f"The Goblin has {self.health} health and {self.power} power.")
        


# values of Hero and Goblins Health and Power
hero = Hero(10, 5)
goblin = Goblin(6, 3)



# Listing our user choices and what happens if they select option 1, 2, or 3
while hero.alive() and goblin.alive():
     hero.print_status()
     goblin.print_status()
     print()
     print("What do you want to do?")
     print("1. Fight Goblin")
     print("2. Do Nothing")
     print("3. Flee")
     print("> ", end="")
     user_input = input()
     if user_input == "1":
        hero.attack(goblin)
        if not goblin.alive():
            print("The goblin is dead. The battle is over!")
     elif user_input == "2":
              if goblin.alive():
                goblin.attack(hero)
     elif user_input == "3":
              print("Goodbye.")
     else:
        print(f"Invalid input {user_input}")









