class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)

    def print_about(self):
        print(f'Лектор {self.name} {self.surname} по курсу {''.join(self.courses_attached)}')

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def print_about(self):
        print(f'Эксперт {self.name} {self.surname} по курсу {''.join(self.courses_attached)}')

lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ['Python']

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

#cool_mentor = Mentor('Some', 'Buddy')
#cool_mentor.courses_attached += ['Python']

#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)

lecturer.rate_hw(best_student, 'Python', 9)
lecturer.rate_hw(best_student, 'Python', 9)
lecturer.rate_hw(best_student, 'Python', 9)

reviewer.rate_hw(best_student, 'Python', 8)
reviewer.rate_hw(best_student, 'Python', 8)
reviewer.rate_hw(best_student, 'Python', 8)

lecturer.print_about()
reviewer.print_about()
print(best_student.grades)