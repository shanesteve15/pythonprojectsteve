
#Exception Handling
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
    print(" finished")

#class is like a blueprint for creating objects

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
student1 = Student(student_id="10",    student_name="John",   student_age="30")
student1.display()




