class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_st_grade(self):
        grades_count = 0
        grades_sum = 0
        for course, grades in self.grades.items():
            grades_count += len(self.grades[course])
            grades_sum += sum(self.grades[course])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def rate_hw(self, lecturer, course, grade_lec):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses:
            if course in lecturer.grades_lec:
                lecturer.grades_lec[course] += [grade_lec]
            else:
                lecturer.grades_lec[course] = [grade_lec]
        else:
            return 'Ошибка'


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
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades_lec = {}
        Lecturer.lecturer_list.append(self)

    def average_lecturer_grade(self):
        grades_count = 0
        grades_sum = 0
        for course, grades in self.grades_lec.items():
            grades_count += len(self.grades_lec[course])
            grades_sum += sum(self.grades_lec[course])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0


class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)



student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Python']

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.courses_attached += ['Python']
student1.rate_hw(lecturer1, 'Python', 7)
student1.rate_hw(lecturer1, 'Python', 7)
student1.rate_hw(lecturer1, 'Python', 7)

reviewer1 = Reviewer('Петр', 'Иванов')
reviewer1.courses_attached += ['Python']

reviewer1.rate_hw(student1,'Python', 10)
reviewer1.rate_hw(student1,'Python', 10)
reviewer1.rate_hw(student1,'Python', 10)


print(student1.grades) # оценки студентов от экспертов
print(student1.average_st_grade())# cредняя оценка у студентов
print(lecturer1.grades_lec) # оценки лекторов
print(lecturer1.average_lecturer_grade())# cредняя оценка у лекторов



