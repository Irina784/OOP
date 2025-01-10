class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_st_grade(self):# cредняя оценка у студентов
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

    def __str__(self):
        some_student = f'Имя:{self.name}\n' \
                       f'Фамилия:{self.surname}\n' \
                       f'Средняя оценка за домашнее задание: {self.average_st_grade()}\n' \
                       f'Курсы в процессе обучения: {', '.join(self.courses_in_progress)}\n' \
                       f'Завершенные курсы: {', '.join(self.finished_courses)}'
        return some_student



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

    def __str__(self):
        some_lecturer = f'Имя:{self.name}\n' \
                        f'Фамилия:{self.surname}\n' \
                        f'Средняя оценка за лекции:{self.average_lecturer_grade()}'
        return some_lecturer

    def __eq__(self, other):
        return self.average_lecturer_grade() == other.average_st_grade()

    def __lt__(self, other):
        return self.average_lecturer_grade() < other.average_st_grade()

    def __le__(self, other):
        return self.average_lecturer_grade() <= other.average_st_grade()


class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

    def __str__(self):
        some_reviewer = f'Имя:{self.name}\n' \
                        f'Фамилия:{self.surname}'
        return some_reviewer


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'GIT']
some_student.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_student.rate_hw(some_lecturer, 'Введение в программирование', 10)
some_student.rate_hw(some_lecturer, 'Введение в программирование', 10)
some_student.rate_hw(some_lecturer, 'Введение в программирование', 9.7)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student,'Python', 10)
some_reviewer.rate_hw(some_student,'Python', 10)
some_reviewer.rate_hw(some_student,'Python', 9.7)


# print(some_student.grades) # оценки студентов от экспертов
# print(some_student.average_st_grade())# cредняя оценка у студентов
# print(some_lecturer.grades_lec) # оценки лекторов
# print(some_lecturer.average_lecturer_grade())# cредняя оценка у лекторов

print(some_reviewer,'\n')
print(some_lecturer,'\n')
print(some_student,'\n')
print(some_lecturer.average_lecturer_grade() == some_student.average_st_grade())
print(some_lecturer.average_lecturer_grade() < some_student.average_st_grade())
print(some_lecturer.average_lecturer_grade() <= some_student.average_st_grade())



