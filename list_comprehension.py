new_product_list = []
products_list = [1, 2, 3, 4, 5]
for item in products_list:  # we will use the .append method to add each item multiply by 2 in the new list.
    new_product_list.append(item * 2)
print(new_product_list)
# the print out will be

products_list = [1, 2, 3, 4, 5, ]
product_list = products_list * 2
print(product_list)

products_list = [1, 2, 3, 4, 5]
new_product_list = [item * 2 for item in products_list]
print(new_product_list)

students = [{'reg_number': 101, 'name': 'Kenny', 'subject': 'python programming Language', 'score': 78},
            {'reg_number': 212, 'name': 'Blessing', 'subject': 'java programming Language', 'score': 65},
            {'reg_number': 322, 'name': 'Ibrahim', 'subject': 'typeScript programming Language', 'score': 87},
            {'reg_number': 434, 'name': 'John', 'subject': 'javaScript programming Language', 'score': 90},
            {'reg_number': 545, 'name': 'Enema', 'subject': 'data analyst', 'score': 35}
            ]

student_name = [student['name'] for student in students]
student_reg_number = [student['reg_number'] for student in students]
print(student_reg_number)
print(student_name)

student_name = [student['name'] for student in students if student['score'] <= 35]
print(student_name)

name = []
input_name = [input("name?") for i in name]
print(input_name)

name_and_score = [{'name': student['name'], 'score': student['score']} for student in students]
print(name_and_score)

no_of_users = len(students)
print(no_of_users)

squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)
squares = [i ** 2 for i in range(1, 11)]
print(squares)

remainder = [x ** 2 % 5 for x in range(1, 5)]
print(remainder)

names_letters = [j for j in students if j['name'].startswith('B')]
print(names_letters)
