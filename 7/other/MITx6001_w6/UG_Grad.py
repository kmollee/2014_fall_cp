from MITPerson import MITPerson


class Student(MITPerson):
    pass


class UG(Student):

    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)

if __name__ == '__main__':
    s1 = UG('Fred', 2016)
    s2 = Grad('Angela')
    print(isStudent(s1))
    print(isStudent(s2))
