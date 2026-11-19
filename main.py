class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def get_grade(self):
        if self.score >= 90:
            
            return "A"
        elif self.score > 79:
            return "B"
        elif self.score > 69:
            return "C"
        elif self.score > 59:
            return "D"
        else:
            return "F"
    
    def display(self):
        print(f"{self.name} - {self.score} - {self.get_grade()}")

student_list = []
    
while True:

    name = str(input("Name: "))
    if not name:
        break
    if not name.replace(" ", "").isalpha():
        print("name should be a string")
        continue
    score = input("score: ")
    if not name or not score:
        break 
    try:
        score = int(score)
    except ValueError:
        print("Score should be a number")
        continue
    student = Student(name, score)
    student_list.append(student)

with open('students.txt', 'a') as file:
    for item in student_list:
        file.write(f"{item.name},{item.score}\n")


with open('students.txt', 'r') as file:
    for lines in file:
        name, score = lines.strip().split(',')
        student = Student(name, int(score))
        print(f"{student.name} - {student.score} - {student.get_grade()}")