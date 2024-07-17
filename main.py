from script import get_random_groups

students = ["Soufiane", "Didier", "Mounir", "Latifa", "Jean-Marc", "Paul", "Kim", "Fatima", "Bilel", "Elyess", "Karim", "Teddy", "Vincent", "Wesley", "Arnaud", "Franck"]

groups = get_random_groups(students)

for i, group in enumerate(groups):
    print(f"GROUPE {i + 1}")
    print("*"*50)
    print('\n')
    print(group)
    print('\n')

