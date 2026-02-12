
class Student:
    def __init__(self,fullname,course,age,feesPaid):
        self.fullname = fullname
        self.course = course
        self.age = age
        self.feesPaid = feesPaid


Student1 = Student("Esther Njoroge","MIT",20,50000)
print(Student1.fullname,Student1.course,Student1.age,Student1.feesPaid)
print()
Student2 = Student("Jane Wanjiku","CyberSecurity",21,60000)
print(Student2.fullname,Student2.course,Student2.age,Student2.feesPaid)
print()
Student3 = Student("David Kamau","DataScience",23,70000)
print(Student3.fullname,Student3.course,Student3.age,Student3.feesPaid)




