# Import random so we can use the function for the hero double damage attack
import random

# Create class Character that the classes of Hero and Goblin will pull from
class Character:
    def __init__(self, health, power, bounty=0):
        self.health = health
        self.power = power
        self.bounty = bounty

# If the character's health is greater than 0, it will return True to being alive.
    def alive(self):
        return self.health > 0
    
# Whenever a character (which is assigned to Hero and Goblin) attacks an enemy, it will print who attacked who and then give back a value of the enemies health
    def attack(self, enemy):
        if enemy.alive():
         damage = self.power
         enemy.health = max(0, enemy.health - damage)  # Prevent health from going negative
         print(f"The {self.__class__.__name__} attacks the {enemy.__class__.__name__}!\n")
         print(f"The {enemy.__class__.__name__}'s health is now {enemy.health}\n")
         if not enemy.alive():
            print(f"The {enemy.__class__.__name__} has been defeated!\n")
        else:
            print(f"The {enemy.__class__.__name__} has already been defeated\n")

    def take_damage(self, damage):
        self.health -= damage


# Add a coins attribute to the Character class. Have it default to a value of 20
    def coins(self, coins = 20):
        self.coins = 20


# Classes of Hero
class Hero(Character):
    def __init__(self, health, power, coins =20):
        super().__init__(health, power, bounty =0)
        self.coins = coins ## Initialize hero with some starting coins
    def print_status(self):
        if self.alive():
         print (f"The Hero has {self.health} health and {self.power} power.\n")
        else:
         print ("GAME OVER\n")

# Make the hero generate double damage points during an attack with a probability of 20%. If random number is less than .2, it will do a default attack.   
    def attack(self, enemy):
        if random.random() < 0.2:
            double_damage = self.power * 2
            enemy.health -= double_damage
            print(f"The {self.__class__.__name__} musters all of his strength and strikes with double damage!\n")
            print(f"The {enemy.__class__.__name__} takes {double_damage} damage!\n")
        else:
            super().attack(enemy)

        # Check if enemy is defeated, if so it will reward the bounty
        if not enemy.alive():
            print(f"You defeated the {enemy.__class__.__name__} and earned {enemy.bounty} coins! Visit the Store to spend.\n")
            self.coins += enemy.bounty  # Add bounty to hero's coins
            print(f"You now have {self.coins} coins.\n")


# Add a buy method to the Hero class so that hero objects can purchase items from a  virtual store
# Give the method an item parameter. The item being purchased will be passed as an arguement into the method.
# It should subtract an items cost from the hero object's avaiable coins
    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)
        

# Class of Goblin
class Goblin(Character):
    def __init__(self, health, power, bounty =5):
        super().__init__(health, power, bounty)

    def print_status(self):
        if self.alive():
            print (f"The Goblin has {self.health} health and {self.power} power.\n")
        

# Class of Shadow 
class Shadow(Character):
    def __init__(self, health, power, bounty =6):
        super().__init__(health, power, bounty)

    def print_status(self):
        print (f"The Shadow has {self.health} health and {self.power} power.\n")

# Only 1 starting health but will only take damage about once out of every ten etimes he is attacked.
    def take_damage(self, amount):
        if random.random() < 0.5:
            self.health -= amount
            print(f"The Shadow takes {amount} of damage!\n")
        else:
         print("The Shadow dodged your attack!\n")


# Class of Zombie
class Zombie(Character):
    def __init__(self, health, power, bounty =20):
        super().__init__(health, power, bounty)

    def print_status(self):
        print (f"The Zombie has {self.health} health and {self.power} power.\n")

# Make the Zombie class not die if it's health reaches zero
    def alive(self):
        return True


# Class of Archer
class Archer(Character):
    def __init__(self, health, power, bounty =10):
        super().__init__(health, power, bounty)

    def print_status(self):
        if self.alive():
         print (f"The Archer has {self.health} health and {self.power} power.\n")


# Class of Wizard
class Wizard(Character):
    def __init__(self, health, power, bounty =15):
        super().__init__(health, power, bounty)

    def print_status(self):
        if self.alive():
         print (f"The Wizard has {self.health} health and {self.power} power.\n")

# values Characters Health and Power
hero = Hero(80, 10)
goblin = Goblin(55, 8, 5)
shadow = Shadow(15, 5, 6)
zombie= Zombie(10, 7, 20)
archer = Archer(25, 6, 10)
wizard = Wizard(35, 15, 15)

# This will check if the characters are alive, and if they are, it  will print their status
while hero.alive():
    print()
    hero.print_status()
    if goblin.alive():
        goblin.print_status()
    else:
        print("The puny Goblin was no match for you\n")
    if shadow.alive():
        shadow.print_status()
    else:
        print("The Shadow could not escape your fury\n")
    if zombie.alive():
        zombie.print_status()
    else:
        print("You just broke the game! WOO HOO!\n")
    if archer.alive():
        archer.print_status()
    else:
        print("You hit the archer from HOW FAR?!\n")
    if wizard.alive():
        wizard.print_status()
    else:
        print("Cordless Hole Punchers don't care about no spells son!\n")
    print()

 # User Choices 
    print("What do you want to do?\n")
    print("1. Fight Goblin")
    print("2. Fight the Shadow")
    print("3. Fight the Zombie")
    print("4. Fight the Archer")
    print("5. Fight the Wizard")
    print("6. Do Nothing")
    print("7. Flee")
    print("> ", end="")
     
     
    user_input = input()
    print()
    if user_input == "1":
        if goblin.alive():
            hero.attack(goblin)
            if goblin.alive():
                goblin.attack(hero)
        else:
            print(f"The {goblin.__class__.__name__} is already dead! Get your head in the game!\n")
    elif user_input == "2":
        if shadow.alive():
            hero.attack(shadow)
            if shadow.alive():
                shadow.attack(hero)
        else:
            print(f"The {shadow.__class__.__name__} is already dead! Get your head in the game!\n")
    elif user_input == "3":
        if zombie.alive():
            hero.attack(zombie)
            zombie.attack(hero)
        else:
            print(f"The {zombie.__class__.__name__} is already dead! Get your head in the game!\n")
    elif user_input == "4":
        if archer.alive():
            hero.attack(archer)
            if archer.alive():
                archer.attack(hero)
        else:
            print(f"The {archer.__class__.__name__} is already dead! Get your head in the game!\n")
    elif user_input == "5":
        if wizard.alive():
            hero.attack(wizard)
            if wizard.alive():
                wizard.attack(hero)
        else:
            print(f"The {wizard.__class__.__name__} is already dead! Get your head in the game!\n")
    elif user_input == "6":
        print("He's just standing there... MENACINGLY!\n")
        if goblin.alive():
            goblin.attack(hero)
        if shadow.alive():
            shadow.attack(hero)
        if zombie.alive():
            zombie.attack(hero)
        if archer.alive():
            archer.attack(hero)
        if wizard.alive():
            wizard.attack(hero)
        print()
        print("Rub some dirt on it champ, and keep your head on a swivel!\n")
    elif user_input == "7":
        print("Throwing in the towel huh? I knew you couldn't handle it!\n")
        break
    else:
        print(f"Uh Oh! Looks like you entered {user_input} instead of a selectable option. Try again!\n")
     
    # Check if the hero has died
    if not hero.alive():
        print("Oh no, The Hero has died! Better luck next time! GAME OVER\n")
        break