
class Student(object):
    name = ""
    def __init__(self, name):
        self.name = name
        
    def printName(self):
        return self.name