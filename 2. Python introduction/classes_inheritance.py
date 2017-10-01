class Student():
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    @classmethod
    # fara classmethod intoarce un obiect Student
    # cu classmethod intoarce un obiect WorxingStudent

    def friend(cls, origin, friendName, salary):
       #return Student(friendName, self.school)
    
    ## se adauga origin pt co nu are access la self si nu poate accesa school
       return cls(friendName, origin.school, salary)
    
# anna = Student('Anna', 'Oxford')
# friend = anna.friend('Greg')
# print(friend.name)
# print(friend.school)


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