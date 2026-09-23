from dataclasses import dataclass
class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
@dataclass
class StudentData:
    name: str
    age: int
s1 = Student("Mou", 22)
s2 = StudentData("Mou", 22)
print("Traditional Class:", s1.name, s1.age)
print("Dataclass:", s2.name, s2.age)