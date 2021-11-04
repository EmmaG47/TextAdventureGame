from rpginfo import RPGInfo
from room import Room
from item import Item
from character import Enemy, Ally

#Game Title and Credits info
buried_temple = RPGInfo("The Buried Temple")
buried_temple.welcome()
RPGInfo.info()
RPGInfo.author = "Raspberry Pi Foundation"

#Room names and descriptions
cave = Room("Cave")
cave.set_description("The map has lead you to an opening in the rockface. Following it further in, you find the remains of the previous adventurer to the caves and a structure beyond.")

temp_en = Room("Temple Entrance")
temp_en.set_description("The cave opens up to a large temple built into the rock, littered with rubble but still showing the markings of what was once intricate detailing.")

temp_hall = Room("Temple Hall")
temp_hall.set_description("Much of the inside has survived. Snake carvings decorate the hall arches and stairwell leading deeper in. Noises tell you the place isn't deserted.")

temp_off = Room("Offering Room")
temp_off.set_description("This room looks to be a kind of offering room, where previous visitors would lay their gifts to the temple deity to show their respects. Unfortunately, it looks like no one has visited in years...")

temp_wor = Room("Worship Room")
temp_wor.set_description("This seems to be the main area of worship for the temple, if the giant deity statue on the back wall is any indication. It appears someone is still lighting the altar candles.")

tomb_en = Room("Tomb Entrance")
tomb_en.set_description("The stairwell lead to some sort of crypt. While there are multiple caskets along the walls, the largest is behind a giant gate. There are two key holes on either side of the gate.")

tomb = Room("Tomb")
tomb.set_description("The gate lifted, you enter the main tomb of the temple. You take a second to look around before the gate slams behind you and a dark presence makes itself known...")

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

#Room links
cave.link_room(temp_en, "east")
temp_en.link_room(cave, "west")

temp_en.link_room(temp_hall, "east")
temp_hall.link_room(temp_en, "west")

temp_hall.link_room(temp_off, "north")
temp_off.link_room(temp_hall, "south")

temp_hall.link_room(temp_wor, "south")
temp_wor.link_room(temp_hall, "north")

temp_hall.link_room(tomb_en, "east")
tomb_en.link_room(temp_hall, "west")

tomb_en.link_room(tomb, "east")
tomb.link_room(tomb_en, "west")

#Item names, descriptions and locations
rh_key = Item("right key")
rh_key.set_description("A white key with a black outlined right hand decorating the head")
rh_key.set_type("Key")

lh_key = Item("left key")
lh_key.set_description("A black key with a white outlined left hand decorating the head ")
lh_key.set_type("Key")
temp_off.set_item(lh_key)

sword = Item("sword")
sword.set_description("A large sword decorated with inscriptions rests on the altar. There is some sort of energy emanating from it.")
sword.set_type("Weapon")
tomb_en.set_item(sword)

bomb = Item("fire bomb")
bomb.set_description("An intact fire bomb found under the body on an unlucky adventurer. Lucky for you, it may come in handy.")
bomb.set_type("Weapon")
cave.set_item(bomb)

shield = Item("shield")
shield.set_description("An old, rotten shield dropped by one of the skeletons. Despite it's age, it still feels solid enough for a fight.")
shield.set_type("Weapon")
temp_en.set_item(shield)

flash = Item("flashlight")
flash.set_description("Your reliable flashlight. Useful for finding loot or useful items in dark corners, which when underground is pretty much everywhere.")
flash.set_type("Backpack Item")

map = Item("map")
map.set_description("The map that helped you find the entrance of the cave")
map.set_type("Backpack Item")

#Enemies
skel_war = Enemy("Skeleton Warrior", "A shambling creature with a sword and shield. It watches you but doesn't attack.")
skel_war.set_conversation("...Leave...")
skel_war.set_weakness("fire bomb")
temp_en.set_character(skel_war)

skel_arc = Enemy("Skeleton Archer", "A shambling creature with a bow and arrow. It shoots at you the second you entered the temple but you are able to dodge the arrows.")
skel_arc.set_conversation("...LEAVE...")
skel_arc.set_weakness("shield")
temp_hall.set_character(skel_arc)

ghost = Enemy("Corrupted Guardian", "Whatever has caused the dark presence to corrupt the temple has also courrupted the ghostly guardian")
ghost.set_conversation("I'm...sorry...")
ghost.set_weakness("sword")
tomb.set_character(ghost)

#Ally
care = Ally("Unknown Woman", "She looks like she's still caring for the temple. She continues her chanting even as you get her attention, her eyes watching your every move")
care.set_conversation("Have you come to pay your respects?")
temp_wor.set_character(care)
care.set_item(rh_key)

#Start game defaults
current_room = cave
backpack = [flash, map]

#Room check loop
game_over = False
while game_over == False:
    print("\n")
    current_room.get_details()
    
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        print("")
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        print("")
        item.describe()

#Movement loop        
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

#Interaction loops        
    elif command in ["talk"]:
        if current_room.get_character() == None:
            print("You're talking to yourself...")
        else: inhabitant.talk()

     
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
           print("What will you fight with?")
           fight_with = input()
           if fight_with in backpack:
               if inhabitant.fight(fight_with) == True:
                   print(inhabitant.name + " is defeated!")
                   current_room.set_character(None)
                   if Enemy.enemies_to_defeat == 0:
                       print("Congratulations, you have purged the temple of the corruption! Hopefully it can be restored back to the state it once was...")
                       game_over = True
               else:
                   game_over = True
                   print("Oh dear, we are in trouble...")
                   print("You could always restart and try again?")
           else:
               print("You don't currently have a " + fight_with)
        elif inhabitant is not None and isinstance(inhabitant, Ally):
            print("They're friendly!")
        else:
            print("There's no one here to fight with!")

            
    elif command == "receive":
        if inhabitant is not None:
            if isinstance(inhabitant, Ally):
                if item is not None:
                    print(inhabitant.name + " gives you a " + item.get_name() + ". You put it in your backpack.")
                    print("The item is a " + item.get_type())
                    backpack.append(item.get_name())
                    inhabitant.set_item(None)
                else:
                    print("Looks like they have nothing to give.")
            else:
                print("Yeah, I don't think they want to give anything...")
        else:
            print("There's no one here to receive a gift from!")


    elif command == "steal":
        if inhabitant is not None:
            if isinstance(inhabitant, Ally):
                if item is not None:
                    print("You steal a " + item.get_name() + "from " +inhabitant.name + ". Luckily they didn't notice!")
                    print("The item is a " + item.get_type())
                    backpack.append(item.get_name())
                    inhabitant.set_item(None)
                else:
                    print("Looks like they have nothing to steal.")
            else:
                print("They're too aggressive to steal from at the moment")
        else:
            print("There's no one here to steal from!")
            
#Item loops
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            print("The item is a " + item.get_type())
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    
RPGInfo.credits()
