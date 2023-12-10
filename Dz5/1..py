class Student:
    def __init__(self, name = "Ivan", age = 18, groupNumber = "10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGroupNumber(self):
        return self.groupNumber
    def setNameAge(self, name, age):
        self.name = name
        self.age = age
    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber


s1 = Student('Владимир', 11, '1Д')
s2 = Student('Катя', 22, '3Г')
s3 = Student('Егор', 11, '7A')
s4 = Student('Инна', 22, '11Б')
s5 = Student('Василий', 33, '7В')

print(s1.getName(), s1.getAge(), s1.getGroupNumber())
print(s2.getName(), s2.getAge(), s2.getGroupNumber())
print(s3.getName(), s3.getAge(), s3.getGroupNumber())
print(s4.getName(), s4.getAge(), s4.getGroupNumber())
print(s5.getName(), s5.getAge(), s5.getGroupNumber())

st = Student()
print(st.getName(), st.getAge(), st.getGroupNumber())
