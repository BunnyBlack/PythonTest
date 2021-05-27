class User:

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"welcome, {self.name}")


class SuperUser(User):

    def __init__(self, name):
        super().__init__(name)

    def welcome(self):
        print(f"welcome, {self.name}, sincerely")
