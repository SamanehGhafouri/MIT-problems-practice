from abc import abstractmethod, ABC


class Animal(ABC):                # Abstract class

    @abstractmethod
    def how_running(self):
        pass


class Horse(Animal):              # Class Horse is inherited from class Animal

    def how_running(self):
        print("with 4 legs")


class Human(Animal):              # Class Human is inherited from class Animal

    def how_running(self):
        print("With 2 legs")


animal1 = Horse()                   # Object of the class Horse
print("how a horse is running: ")
animal1.how_running()

animal2 = Human()                   # Object of the class Human
print("how a human is running: ")
animal2.how_running()

animalz = Animal()                  # Object of the class Animal which will give error because
animalz.how_running()               # an abstract class cant be instantiated



