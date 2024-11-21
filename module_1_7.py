grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_1 = sorted(students) #нашёл функцию сортировки по алфавиту
print(students_1) # проверка

# объединяем имена и оценки в один список
успеваемость = (students_1[0], grades[0],
                students_1[1], grades[1],
                students_1[2], grades[2],
                students_1[3], grades[3],
                students_1[4], grades[4])
print(успеваемость) # проверяем

# вычисляем средний бал студентов:
средний_бал_студента = (sum(grades[0]) / len(grades[0]),
                        sum(grades[1]) / len(grades[1]),
                        sum(grades[2]) / len(grades[2]),
                        sum(grades[3]) / len(grades[3]),
                        sum(grades[4]) / len(grades[4]))
print(средний_бал_студента) # проверяем

# создадам словарь: имена студентов и их средний бал
Студент_средний_бал = {students_1[0]: sum(grades[0]) / len(grades[0]),
                       students_1[1]: sum(grades[1]) / len(grades[1]),
                       students_1[2]: sum(grades[2]) / len(grades[2]),
                       students_1[3]: sum(grades[3]) / len(grades[3]),
                       students_1[4]: sum(grades[4]) / len(grades[4])}
print(Студент_средний_бал)