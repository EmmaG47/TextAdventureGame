
class Item():
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.type = None

#Item Name
    def set_name(self, item_name):
        self.name = item_name
    
    def get_name(self):
        return self.name

#Item Description
    def set_description(self, item_description):
        self.description = item_description
        
    def get_description(self):
        return self.description

#Item Type
    def set_type(self, item_type):
        self.type = item_type
        
    def get_type(self):
        return self.type

#Describe Item
    def describe(self):
        print("There's a " + self.name + " here! " + self.description)
