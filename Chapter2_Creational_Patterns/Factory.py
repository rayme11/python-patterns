class Dog:
    """A simple dog class """

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"

    def name(self):
        return self.name

    def sosoSkill(self):
        print("I am kind of fun sometimes")

class Cat:
    """A simple cat class """

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"

    def name(self):
        return self.name

    def amazingSkill(self):
        print('I jump super high')


def get_pet(pet="cat"):
    """ The Factory Method"""

    pets = dict(dog=Dog("La Bola"), cat=Cat("Pumpkin"))
    return pets[pet]


d = get_pet("dog")
print(d.speak())
print(d.name)
d.sosoSkill()

c = get_pet("cat")
print(c.speak())
print(c.name)
c.amazingSkill()
