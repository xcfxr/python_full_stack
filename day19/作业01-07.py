usr_info = []
with open('db.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        name, sex, age, salary = line.split(' ')
        usr_info.append({'name': name, 'sex': sex, 'age': age, 'salary': salary})

