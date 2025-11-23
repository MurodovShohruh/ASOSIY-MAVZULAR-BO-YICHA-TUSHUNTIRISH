# # 1-vazifa: Person class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         return f"Ism: {self.name}, Yosh: {self.age}"
        

# # test
# p = Person("Ali", 20)
# print(p.info())

# # yoki initsiz class 
# class Person:
#     def info(self):
#         return f"Ism: {self.name}, Yosh: {self.age}"

# # obyekt yaratish
# p = Person()

# # instance atributlarini to‘g‘ridan-to‘g‘ri berish
# p.name = "Ali"
# p.age = 20

# print(p.info())

# # 2-vazifa
# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade

#     def get_grade(self):
#         return f"Ismi {self.name},talaba {self.grade}"

# s=Student("Alia","4-kurs")

# print(s.get_grade())

class Employee:
    count = 0  # class attribute

    def __init__(self, name):
        self.name = name       # instance attribute
        Employee.count += 1    # har yangi obyekt yaratilganda +1

# Test
e1 = Employee("Ali")
e2 = Employee("Vali")
e3 = Employee("Olim")

print(Employee.count)  # 3
