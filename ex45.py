## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a kind of Animal
class Dog(Animal):

    def __init__(self, name):
        ##
        self.name = name


## Cat is-a kind of Animal
class Cat(Animal):

    def __init__(self, name):
        ##
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ##
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Emploee is-a kind of Person
class Emploee(Person):

    def __init__(self, name, salary):
        ## hmm what is this strange magic
        super(Emploee, self).__init__(name)
        ## 
        self.salary = salary

##
class Fish(object):
    pass

##
class Salmon(Fish):
    pass

##
class Halibut(Fish):
    pass

## rover is a dog
rover = Dog("Rover")

##
satan = Cat("Satan")

##
mary = Person("Mary")
mary.pet = satan

frank = Emploee("Frank", 120000)
frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
