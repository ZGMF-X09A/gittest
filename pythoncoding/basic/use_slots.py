class Student(object):
    __slots__ = ('name', 'age')    
s = Student()
s.name = 'Michael'
s.age = 18
s.score = 99