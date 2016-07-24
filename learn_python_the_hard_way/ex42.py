## Animal is-an Object
class Animal(object):
    pass

## Dog is-an Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-an Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-an Object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name
        
        ## Person has-a pet
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## 
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-an Object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet, "satan"
mary.pet = satan

## frank is-an employee, with salary $120,000
frank = Employee("Frank", 120000)

## frank has-a pet, "rover"
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()
