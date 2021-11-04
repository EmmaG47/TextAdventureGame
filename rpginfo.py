
class RPGInfo():
    def __init__(self, game_title):
        self.title = game_title
        author = "Anon"

    def welcome(self):
        print("Welcome to " + self.title)

    @staticmethod
    def info():
        print("Made using the OOP RPG game creator (c) me")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)
