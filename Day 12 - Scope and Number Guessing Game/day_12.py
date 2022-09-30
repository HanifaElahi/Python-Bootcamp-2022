################################## Scope ##################################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope exists within Function
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
print(potion_strength)

# Global Scope can be excessible anywhere

# Global Scope
player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()


print(player_health)

# There is no Block Scope in Python
""" This simple means that if u create a variable inside a function then that variable is going to have a local scope but if u create a variable inside if statement or for loop or else then it won't have such local scope"""

game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


#################### Modifying a Global Variable ####################

enemies = 1


def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Preferred Method to Modify Global Scope

enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
