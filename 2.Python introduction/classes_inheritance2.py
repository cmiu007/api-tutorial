class Student():
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    @classmethod
    def friend(cls, origin, friendName, *args):
       return cls(friendName, origin.school, *args)



##

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary



anna = WorkingStudent('Anna', 'Oxford', 20.00)
# anna este origin pt school
friend = WorkingStudent.friend(anna, 'Greg', 10.00)

print('Anna salary is {}'.format(anna.salary))
print('{} salary is {}'.format(friend.name, friend.salary))


##
class WorkingStudent2(Student):
    def __init__(self, name, school, salary, jobTitle):
        super().__init__(name, school)
        self.salary = salary
        self.jobTitle = jobTitle
        # adaugam o noua proprietate fara a modifica clasa Student
        # datorita *args


friend2 = WorkingStudent2.friend(anna, 'Greg', 10.00, 'Software Developer')
print(friend2.jobTitle)


##


class Student2():
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    @classmethod
    def friend(cls, origin, friendName, **kwargs):
       return cls(friendName, origin.school, **kwargs)



class WorkingStudent3(Student2):
    def __init__(self, name, school, salary, jobTitle):
        super().__init__(name, school)
        self.salary = salary
        self.jobTitle = jobTitle
        # adaugam o noua proprietate fara a modifica clasa Student
        # datorita *args


friend3 = WorkingStudent3.friend(anna, 'Greg', salary=10.00, jobTitle='Software Developer')
print(friend3.jobTitle)