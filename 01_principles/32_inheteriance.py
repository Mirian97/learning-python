class Animal:
    def walk(self):
        print("Walk")
        
class Dog(Animal):
    def bark(self):
        print("Au Auu")
        
dog = Dog()
dog.bark()
dog.walk()