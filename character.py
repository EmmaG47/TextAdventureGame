class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.item = None
        
    # Describe this character
    def describe(self):
        print( " It's " + self.name + " !" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    #Character item
    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item
    
class Enemy(Character):
    enemies_to_defeat = 0
    
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.item = None
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1

    #Enemy Weakness
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1           
            return True
        else:
            print(self.name + " strikes you down where you stand")
            return False

class Ally(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        
    #Ally Assistance - gift, steal, information
    def gift(self, gift_item):
        print(self.name + "gives you " + self.item)

    def steal(self):
        print("You steal from " + self.name)
        print("You obtain " + self.item + "and put it in your backpack.")
        
