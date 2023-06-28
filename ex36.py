from sys import exit
from sys import argv

'''
game will random generated dungeon
use double array to form a grid and assign rooms/functions to each room
take user input to go in a cardinal direction
keep track to player's stats health, attack, defense

'''

attack = 10
def treasure_room():
    print("")


def monster_room():
    print("")
    health = 10

    choice = input("> ")
    while health > 0:
        if "attack" in choice:
            health -= attack

def boss_room():
    print("")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "attack" in choice:
        health -= attack
    else:
        boss_room()

def dead(why):
    print(why, "Try again")
    exit(0)

def start():
    print("you are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "north":
      monster_room()
    elif choice == "south":
      monster_room()
    elif choice == "east":
      monster_room()
    elif choice == "west":
      monster_room()
    else:
      dead("You stumble around the room until you starve.")



start()
