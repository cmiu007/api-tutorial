class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        print('Self: I m going to {}.'.format(self.school))
    
    #da eroeare
    # def go_to_school_generic():             
    #     print('I m goinge to school')

    #corect
    @classmethod
    def go_to_school_generic(cls):
        print('ClassMethod: I m going to school')
    #or

    @staticmethod
    def go_to_school_generic2():
        print('Static method: I m going to school')

anna = Student('Anna', 'MIT')
anna.marks.append(56)
anna.marks.append(1)
# print(anna.average())


anna.go_to_school()
# pt class methond
anna.go_to_school_generic()
# sau
Student.go_to_school_generic()


# pt static
Student.go_to_school_generic2()
