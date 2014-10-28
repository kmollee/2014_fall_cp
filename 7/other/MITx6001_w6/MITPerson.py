from person import Person


class MITPerson(Person):
    nextIdNum = 0  # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name)  # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum
    # sorting MIT people uses their ID number, not name

    def __lt__(self, other):
        return self.idNum < other.idNum

if __name__ == '__main__':
    p1 = MITPerson('Eric')
    p2 = MITPerson('John')
    p3 = MITPerson('John')
    p4 = Person('John')

    # print(p1)
    # p1.getIdNum()
    # p2.getIdNum()
    # p1 < p2
    # p3 < p2
    # p4 < p1

    # p1 < p4
