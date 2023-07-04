from sys import exit
from sys import argv

'''
game will random generated dungeon
use double array to form a grid and assign rooms/functions to each room
take user input to go in a cardinal direction
keep track to player's stats health, attack, defense

'''

player_attack = 10
player_health = 100
player_defense = 10

dungeon = [[1,1,2,0,0],
            [2,1,1,1,2],
            [0,0,1,2,0],
            [2,1,1,0,0],
            [0,0,1,1,3]]
x = 0
y = 0
def treasure_room():
    print("You found a treasure room!/nWhat will you take?/n1. Sword/n2. Armor/n3. Golden Apple")

    choice = input("> ")

    try:
        how_much = int(choice)
    except ValueError:
        dead("Man, learn to type a number.")

    if(choice == 1):
        player_attack += 50
    elif(choice == 2):
        player_defense += 50
    elif(choice == 3):
        player_health += 100
    else:
        print("You didn't get anything.")

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

def no_room():


def room(room_num):
    if room_num = 1:
        return monster_room()
    elif room_num = 2:
        return treasure_room()
    elif room_num = 3:
        return boss_room()
    else:
        return no_room()

def location(dir_x, dir_y):
    x += dir_x
    y += dir_y

    return room(dungeon[x,y])

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
