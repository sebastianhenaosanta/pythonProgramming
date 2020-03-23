
class Student(object):
    name = ""
    code = ""
    def __init__(self, code, name):
        self.name = name
        self.code = code
    
    def getCode(self):
        return self.code
    
    def getName(self):
        return self.name