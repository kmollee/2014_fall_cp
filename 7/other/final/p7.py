"""
A Frob is an object that has a name, and two connections or links: a "before" and an "after" link that are intended to point to other instances of objects.

We can use Frobs to form a data structure called a doubly linked list. In a doubly linked list, each element has the property that if element A has a "before" link to element B, then element B has an "after" link to element A. We want to create a doubly linked collection of Frob instances with the property that all Frobs with names that are alphabetically before a specific Frob's name appear ordered along the "before" link, and all Frobs with names that are alphabetically after a specific Frob's name appear ordered along the "after" link.
"""


class Frob(object):

    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None

    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before

    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after

    def getBefore(self):
        return self.before

    def getAfter(self):
        return self.after

    def myName(self):
        return self.name

    def setConnect(self, f1, f2):
        self.setBefore(f1)
        f1.setAfter(self)
        self.setAfter(f2)
        f2.setBefore(self)


def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    before, me, after = atMe.getBefore(), atMe, atMe.getAfter()
    # grater than me
    if newFrob.myName() > me.myName():
        # if me.after is none
        if after is None:
            me.setAfter(newFrob)
        # not none, compare each
        else:
            # if newForn greater than after
            if after.myName() < newFrob.myName():
                after.setConnect(me, newFrob)
            else:
                newFrob.setConnect(me, after)
    # less than me
    else:
        if before is None:
            me.setBefore(newFrob)
        else:
            if before.myName() > newFrob.myName():
                before.setConnect(newFrob, me)
            else:
                newFrob.setConnect(before, me)


def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    if start.before is None:
        return start
    return findFront(start.before)

if __name__ == '__main__':
    eric = Frob('eric')
    andrew = Frob('andrew')
    ruth = Frob('ruth')
    fred = Frob('fred')
    martha = Frob('martha')

    insert(eric, andrew)
    insert(eric, ruth)
    insert(eric, fred)
    insert(ruth, martha)

    print(findFront(eric).myName())
