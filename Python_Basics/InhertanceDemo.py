class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def annoy(self):
        print("annoy")

dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.walk()
cat1.annoy()