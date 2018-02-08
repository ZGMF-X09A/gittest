class Student(object):
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda :25
        else:
            raise AttributeError('object Student does not have attribute \'%s\'' % attr)
s = Student()
print(s.age())
s.name