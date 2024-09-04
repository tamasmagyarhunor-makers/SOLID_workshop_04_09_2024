### SOLID

## - Single Responsibility Principle*
## - Open/Closed Principle
## - Liskovs Substitution Principle
## - Interface Seggregation Principle
## - Dependency Inversion Principle

## Single Responsibility Principle
### wrong code below
class WriteObject():
    def __init__(self, type):
        self.type = type

pencil = WriteObject('pencil')

notebook = Notebook(pencil)
notebook.write('hi my dear calendar')

class Notebook():
    def __init__(self, write_object):
        self.write_object = write_object
    
    def write(self, text):
        if self.write_object.type == "ball pen":
            self.__turn_on(self.write_object)
            return text
        elif self.write_object.type == "ink pen":
            if self.__has_enough_ink(self.write_object):
                return text
            else:
                self.__refill_ink(self.write_object)
                return text
        elif self.write_object.type == 'pencil':
            if self.__sharp_enough(self.write_object):
                return text
            else:
                self.__sharpen(self.write_object)
                return text
        else:
            raise Exception("need some write object to write")
            
    # private methods
    def __sharpen(write_object):
        # sharpen the pencil
        pass

    def __refill_ink(write_object):
        # refill ink
        pass

    def __sharp_enough(write_object):
        # check if pencil is sharp enough
        pass


    def __has_enough_ink(write_object):
        # check if ink pen it has enough ink
        pass

    def __turn_on(write_object):
        #press the top of the ball pen to turn it on
        pass

## good code below
class WriteObject(): # abtract, so should not be instantiated
    def __init__(self):
        raise Exception('WriteObject cant be instantiated')
    
    def write(self, text):
        raise Exception('WriteObject cant write, please instantiate a Pencil, Ink Pen or Ball Pen')
    

class Pencil(WriteObject):
    def __init__(self):
        pass

    def write(self, text):
        if self.__sharp_enough():
            return text
        else:
            self.__sharpen()
            return text
        
    # private
    def __sharp_enough(self):
        # check if the pencil is sharp enough
        pass

    def __sharpen(self):
        # sharpen the pencil
        pass

class BallPen(WriteObject):
    def __init__(self):
        pass

    def write(self, text):
        self.__turn_on()
        return text
    
    #private
    def __turn_on():
        # turn on the ball pen
        pass


class InkPen(WriteObject):
    def __init__(self):
        pass

    def write(self, text):
        if self.__has_enough_ink():
            return text
        else:
            self.__refill_ink()
            return text
#private
    def __has_enough_ink(self):
        # check if there is enough ink
        pass

    def __refill_ink(self):
        # refill the ink
        pass

class Notebook():
    def __init__(self, write_object: WriteObject):
        self.write_object = write_object

    def write(self, text):
        return self.write_object.write(text)



# Open/Closed Principle
# bad code
class Building():
    def __init__(self):
        pass

    def check_in(self, person, lanyard):
        # check lanyard
        # let person in if lanyard valid
        pass

# MI6 works in the building, security check at check-in has to be improved/changed

class BuildingCheckIn():
    def __init__(self):
        pass

    def check_in(self, person, lanyard):
        # check lanyard
        # let person in if lanyard valid
        pass

class BuildingCheckInMI6(BuildingCheckIn):
    def check_in(self, person, lanyard, mi6_id):
        # check lanyard
        # check mi6 id
        # let person in if lanyard and mi6 id is valid
        pass


class Building():
    def __init__(self):
        self.checkin = BuildingCheckIn
        self.checkin_mi6 = BuildingCheckInMI6

    def let_in_people(self):
        return self.checkin.check_in(person, lanyard)

    def let_in_mi6_people(self):
        return self.checkin.check_in(person, lanyard, mi6_id)
    

# Liskovs Substitution Principle
class Person():
    def __init__(self):
        raise Exception("Please implement your classes own __init__ function. Person object SHOULD NOT be instantiated. It acts only as an Abstract class")
    
    def how_i_drink_my_coffee(self):
        raise Exception(f"Please implement drink_coffee() for {self.__class__}")
    
class Linh(Person):
    def __init__(self):
        pass

    def how_i_drink_my_coffee(self):
        return "latte with 2 sugar and cocoa on top"

class Adebayo(Person):
    def __init__(self):
        pass

    def how_i_drink_my_coffee(self):
        return "americano, no sugar"

class Elizabeth(Person):
    def __init__(self):
        pass

    def how_i_drink_my_coffee(self):
        return "f*** coffee, give me a breakfast tea please"

class CoffeeShop():
    def __init__(self):
        pass

    def make_coffee_for(person: Person):
        coffee = person.how_i_drink_my_coffee()
        #some logic to interpret the coffee making instructions and make THAT, EXACT coffee
        return coffee # your coffee the way you have it

class World():
    def __init__(self):
        self.persons = []
        self.coffee_shop = CoffeeShop()

    def add_person(self, person: Person):
        self.persons.append(person)

    def get_coffee_for_person(self, person: Person):
        return self.coffee_shop.make_coffee_for(person)


# Interface Seggregation Principle
## bad code
class Person():
    def __init__(self):
        pass

    def check_in(self, visitor, safety_rules):
        pass

class MakersEmployee(Person):
    pass

class MakersStudent(Person):
    pass

## good code
class Person():
    def __init__(self):
        pass

    # other functions

class MakersEmployee(Person):
    def check_in(self, visitor, safety_rules):
        pass

class MakersStudent(Person):
    pass

## Dependency Inversion principle
  ### Classes should depend on abstractions not concretions

  ### Depency Inversion principle NOT respected
class Base64Hasher():
    # hashing password with 64bit security
    def hash_password(string):
        # hashes the string with 64bit security
        # returns the string
        pass

class Base128Hasher():
    def hash_password(string):
        # hashes the string with 64bit security
        # returns the string
        pass

class Base256Hasher():
    def hash_password(string):
        # hashes the string with 64bit security
        # returns the string
        pass

class PasswordService():
    def __init__(self):
        if year == '2023':
            self.hasher = Base64Hasher()
        elif year == '2024':
            self.hasher = Base128Hasher()

    def hash(self, string):
        return self.hasher.hash_password(string)
    
## good code
class PasswordService():
    def __init__(self, hasher):
        self.hasher = hasher

    def hash_password(self, string):
        return self.hasher.hash_password(string)

hasher = Base64Hasher()
pw_service = PasswordService(hasher)
pw_service.hash('myverysecurepassword13091988@')

hasher = Baser1024Hasher()
pw_service = PasswordService(hasher)