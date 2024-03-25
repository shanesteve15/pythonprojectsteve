
#Exception Handling
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
    print(" finished")

#class is like a blueprint for creating object
class Student:
      student_id = 0
      student_name = ""
      student_age = 0
      def __init__(self, student_id, student_name, student_age):
          self.student_id = student_id
          self.student_name =student_name
          self.student_age =student_age
      def display(self):
          print("Student details are:""Name:",self.student_name,   "Age:",self.student_age,   "Student ID:",self.student_id)
student1 = Student(  "10",    "John",  "30")
student1.display()


#Python Inheritance
class person:
    person_age = 0
    person_name = ""
    person_residence=""
    def __init__(self, person_age, person_name, person_residence):
        self.person_age = person_age
        self.person_name = person_name
        self.person_residence = person_residence
    def print_info(self):
        print("person_age:",self.person_age, "person_name:",self.person_name, "person_residence:",self.person_residence)

class student(person):
    uniform=""
    def __init__(self,name,age,residence,uni):
        super().__init__(name,age,residence)
        self.uniform=uni
        print("Uniform:",self.uniform)

student1 = student("46", "kamau", "380", "blue")
student1.print_info()


#Polymorphism
class animal:
    limbs=4
    eyes=2
    def __init__(self,limbs,eyes):
        self.limbs=limbs
        self.eyes=eyes
        print ("limbs:",self.limbs,"eyes:",self.eyes)
    def speak(self):
        pass
class Dog(animal):
    def speak(self):
        print("I am a dog and i bark")
class Cat(animal):
    def speak(self):
     print("I am a cat and i meow")
dog1=Dog(limbs=4 , eyes=2)
dog1.speak()
cat1=Cat(limbs=4 , eyes=2)
cat1.speak()







