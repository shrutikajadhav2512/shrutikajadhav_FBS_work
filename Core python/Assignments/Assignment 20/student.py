from SY.SYMARKS import SYMARKS
from TY.TYMarks import TYMarks


class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def display_result(self):

        total = (
            self.sy_marks.ComputerTotal
            + self.ty_marks.Theory
            + self.ty_marks.Practical
        )

        percentage = (total / 300) * 100

        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("---------- Student Result ----------")
        print("Roll No     :", self.roll_no)
        print("Name        :", self.name)
        print("Computer    :", total)
        print("Percentage  :", percentage)
        print("Grade       :", grade)


# SYMarks object
sy = SYMARKS(75, 65, 70)

# TYMarks object
ty = TYMarks(80, 70)

# Student object
student = Student(101, "Rahul", sy, ty)

# Display result
student.display_result()
