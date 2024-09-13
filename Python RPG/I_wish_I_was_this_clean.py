# Import random so we can use the function for the hero's double damage attack
import random

# Create class Character that the Hero and Goblin classes will inherit from
class Character:
    def __init__(self, health, power, bounty=0):
        self.health = health
        self.power = power
        self.bounty = bounty

    # Check if the character is alive
    def alive(self):
        return self.health > 0

    # Attack method for the characters
    def attack(self, enemy):
        if enemy.alive():
            damage = self.power
            enemy.health = max(0, enemy.health - damage)  # Prevent health from going negative
            print(f"The {self.__class__.__name__} attacks the {enemy.__class__.__name__}!")
            print(f"The {enemy.__class__.__name__}'s health is now {enemy.health}")
            
            if not enemy.alive():
                print(f"The {enemy.__class__.__name__} has been defeated!\n")
        else:
            print(f"The {enemy.__class__.__name__} is already dead!\n")

    # Taking damage
    def take_damage(self, damage):
        self.health -= damage

    # Coins attribute with a default value of 20
    def coins(self, coins=20):
        self.coins = coins


# Hero class
class Hero(Character):
    def __init__(self, health, power, coins=20):
        super().__init__(health, power, bounty=0)
        self.coins = coins  # Initialize hero with some starting coins

    def print_status(self):
        if self.alive():
            print(f"The Hero has {self.health} health and {self.power} power.\n")
        else:
            print("GAME OVER\n")

    # Hero's attack with a chance of double damage (20%)
    def attack(self, enemy):
        if random.random() < 0.2:
            double_damage = self.power * 2
            enemy.health -= double_damage
            print(f"The {self.__class__.__name__} strikes with double damage!")
            print(f"The {enemy.__class__.__name__} takes {double_damage} damage!\n")
        else:
            super().attack(enemy)

        # If enemy is defeated, reward the hero with coins
        if not enemy.alive():
            print(f"You defeated the {enemy.__class__.__name__} and earned {enemy.bounty} coins!")
            self.coins += enemy.bounty  # Add bounty to hero's coins
            print(f"You now have {self.coins} coins.\n")

    # Buying items from a store
    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)


# Goblin class
class Goblin(Character):
    def __init__(self, health, power, bounty=5):
        super().__init__(health, power, bounty)

    def print_status(self):
        if self.alive():
            print(f"The Goblin has {self.health} health and {self.power} power\n")


# Shadow class
class Shadow(Character):
    def __init__(self, health, power, bounty=6):
        super().__init__(health, power, bounty)

    def print_status(self):
        print(f"The Shadow has {self.health} health and {self.power} power\n")

    # Shadow takes damage only half the time
    def take_damage(self, amount):
        if random.random() < 0.5:
            self.health -= amount
            print(f"The Shadow takes {amount} damage!\n")
        else:
            print("The Shadow dodged your attack!\n")


# Zombie class
class Zombie(Character):
    def __init__(self, health, power, bounty=20):
        super().__init__(health, power, bounty)

    def print_status(self):
        print(f"The Zombie has {self.health} health and {self.power} power\n")

    # Zombies never die!
    def alive(self):
        return True


# Archer class
class Archer(Character):
    def __init__(self, health, power, bounty=10):
        super().__init__(health, power, bounty)

    def print_status(self):
        if self.alive():
            print(f"The Archer has {self.health} health and {self.power} power\n")


# Wizard class
class Wizard(Character):
    def __init__(self, health, power, bounty=15):
        super().__init__(health, power, bounty)

    def print_status(self):
        if self.alive():
            print(f"The Wizard has {self.health} health and {self.power} power\n")


# Function to handle a fight between hero and enemy
def handle_fight(hero, enemy):
    if enemy.alive():
        hero.attack(enemy)
        if enemy.alive():
            enemy.attack(hero)
    else:
        print(f"The {enemy.__class__.__name__} is already dead! Get your head in the game!\n")


# Instantiate the characters
hero = Hero(100, 10)
goblin = Goblin(55, 8)
shadow = Shadow(15, 5)
zombie = Zombie(10, 7)
archer = Archer(25, 6)
wizard = Wizard(35, 15)

# Main game loop
while hero.alive():
    print()
    hero.print_status()
    
    if goblin.alive(): goblin.print_status()
    else: print("The puny Goblin was no match for you\n")

    if shadow.alive(): shadow.print_status()
    else: print("The Shadow could not escape your fury\n")

    if zombie.alive(): zombie.print_status()
    else: print("You just broke the game! WOO HOO!\n")

    if archer.alive(): archer.print_status()
    else: print("You hit the archer from HOW FAR?!\n")

    if wizard.alive(): wizard.print_status()
    else: print("Cordless Hole Punchers don't care about no spells son!\n")

    print("What do you want to do?\n")
    print("1. Fight Goblin")
    print("2. Fight the Shadow")
    print("3. Fight the Zombie")
    print("4. Fight the Archer")
    print("5. Fight the Wizard")
    print("6. Do Nothing")
    print("7. Flee")
    print("> ", end="")
     
    user_input = input().strip()
    print()

    if user_input == "1":
        handle_fight(hero, goblin)
    elif user_input == "2":
        handle_fight(hero, shadow)
    elif user_input == "3":
        handle_fight(hero, zombie)
    elif user_input == "4":
        handle_fight(hero, archer)
    elif user_input == "5":
        handle_fight(hero, wizard)
    elif user_input == "6":
        print("He's just standing there... MENACINGLY!\n")
        if goblin.alive(): goblin.attack(hero)
        if shadow.alive(): shadow.attack(hero)
        if zombie.alive(): zombie.attack(hero)
        if archer.alive(): archer.attack(hero)
        if wizard.alive(): wizard.attack(hero)
        print("Rub some dirt on it champ, and keep your head on a swivel!\n")
    elif user_input == "7":
        print("Throwing in the towel huh? I knew you couldn't handle it!\n")
        break
    else:
        print(f"Uh Oh! Looks like you entered {user_input} instead of a selectable option. Try again!\n")
     
    if not hero.alive():
        print("Oh no, The Hero has died! Better luck next time! GAME OVER\n")
        break