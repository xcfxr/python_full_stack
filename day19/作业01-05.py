usr_info = []
with open('./db.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        name, sex, age, salary = line.strip().split(' ')
        usr_info.append({'name': name, 'sex': sex, 'age': age, 'salary': salary})

sum_of_salary = sum(int(usr['salary']) for usr in usr_info)
print(sum_of_salary)
name_of_men = [usr['name'] for usr in usr_info if usr['sex'] == 'male']
print(name_of_men)
for usr in usr_info:
    usr['name'] = usr['name'].capitalize()
print(usr_info)
print(list(filter(lambda x: not x['name'].startswith('a'), usr_info)))

