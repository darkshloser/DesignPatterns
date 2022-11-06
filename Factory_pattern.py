from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface method """

class Student(IPerson):

    def __init__(self):
        self.name = "Basic student name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I'm a teacher")

# s1 = Student()
# s1.person_method()

# t1 = Teacher()
# t1.person_method()

# if we want to decide dinamically what person to be created. We can do it by 
# creating a Factory class 

class PersonFactory:
    
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        elif person_type == 'Teacher':
            return Teacher()
        print("Invalid type")
        return -1

if __name__ == "__main__":
    choice = input("What type of person you want to create ?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()