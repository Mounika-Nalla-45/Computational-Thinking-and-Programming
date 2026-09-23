## 6. Student Data Model: Dataclass vs Traditional Class

### Aim

To implement a student data model using Dataclasses and compare it with
a traditional class implementation in Python.

### Algorithm

1.  Create a traditional class with an initializer.
2.  Create a dataclass with the same attributes.
3.  Create objects using both implementations.
4.  Display the stored data.
5.  Compare code simplicity and readability.

### Python Program

``` python
from dataclasses import dataclass


# Traditional class
class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


# Dataclass
@dataclass
class StudentData:
    name: str
    age: int


# Create objects
s1 = Student("Mou", 22)
s2 = StudentData("Mou", 22)

print("Traditional Class:", s1.name, s1.age)
print("Dataclass:", s2.name, s2.age)
```

### Data (Input)

``` text
Student name: Ravi
Student age: 20
Implementations: Traditional Class and Dataclass
```

### Result (Output)

``` text
Traditional Class: Ravi 20
Dataclass: Ravi 20
```

### Inference

Dataclasses reduce boilerplate code and make data models easier to read
and maintain.

### Analysis

  Feature          Traditional Class   Dataclass
  ---------------- ------------------- -------------------------
  Initialization   Manually written    Automatically generated
  Code length      More                Less
  Readability      Moderate            High
  Type Hints       Supported           Supported

-   Time complexity: `O(1)` for creating and accessing a fixed-size
    object.
-   Space complexity: `O(1)` per object, excluding memory used by
    variable-sized attribute values.
-   Conclusion: Dataclasses simplify data modeling compared to
    traditional classes.
