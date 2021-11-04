
class Room():

    number_of_rooms = 0
    
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        
        Room.number_of_rooms = Room.number_of_rooms + 1

#Room Description
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

#Room Name
    def set_name(self, room_name):
        self.name = room_name
       
    def get_name(self):
        return self.name

#Character in Room
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

#Item in Room
    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item

#Describe the Room
    def describe(self):
        print( self.description )

#Linking Rooms
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

#Display Details
    def get_details(self):
        print(self.name)
        print("------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print ( "The " + room.get_name() + " is " + direction)

#Move method
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("A wall blocks your progress - you cannot leave this way")
            return self


        

