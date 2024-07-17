import random

list_group = [[] for x in range(4)]

def get_random_groups(students):
    for _ in range(len(students)):
        for i in range(len(list_group)):
            el = random.choice(students)
            if len(list_group[0]) < 4 and el not in list_group[0]:
                list_group[0].append(el)
                if el in students:
                    students.remove(el)
        for i in range(len(list_group)):
            el = random.choice(students)
            if len(list_group[1]) < 4 and el not in list_group[1]:
                list_group[1].append(el)
                if el in students:
                    students.remove(el)
        for i in range(len(list_group)):
            el = random.choice(students)
            if len(list_group[2]) < 4 and el not in list_group[2]:
                list_group[2].append(el)
                if el in students:
                    students.remove(el)
        list_group[3] = students
    return list_group


