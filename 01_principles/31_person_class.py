class Person:
    def __init__(self, name: str):
        self.name = name;
        
    def talk(self):
        print(f"Hi, I'm {self.name}.")
        
person = Person("Mirian")
print(person.name)
person.talk()