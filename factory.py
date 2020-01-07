class Person:
    def __init__(self):
        self.name=None
        self.gender=None
    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
class Male(Person):
    def __init__(self,name):
        print("hello mr."+name)
class Female(Person):
    def __init__(self,name):
        print("hello miss."+name)
class Factory:
    def getPerson(self,name,gender):
        if gender=='M':
            return Male(name)
        if gender=='F':
            return Female(name)
if __name__=='__main__':
    factory=Factory()
    list=[["Ali","M"],["Sena","F"]]
    for i in list:
        person=factory.getPerson(i[0],i[1])                         

