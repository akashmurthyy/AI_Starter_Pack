class Person:
    def __init__(self, name):
       self.name = name
    def talk(self):
        print(f'Hi! I am {self.name}')


person1 = Person("Altman")
print(person1.name)
person1.talk()