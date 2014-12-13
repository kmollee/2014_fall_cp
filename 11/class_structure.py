class Structure:
    _fields = []

    def __init__(self, *args):
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

"""
class Stock:
    def __init__(self,x,y):
        self.x = x
        self.y = y
"""


class Stock(Structure):
    _fields = ['name', 'share', 'price']
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
"""


class Point(Structure):
    _fields = ['x', 'y']

"""
class Address:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
"""


class Address(Structure):
    _fields = ['hostname', 'port']
