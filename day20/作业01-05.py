usr_info = []
with open('./db.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        name, sex, age, salary = line.strip().split(' ')
        usr_info.append({'name': name, 'sex': sex, 'age': age, 'salary': salary})


rich = max(usr_info, key=lambda x:x['salary'])
print(rich)
young = min(usr_info, key = lambda x:x['age'])
print(young)

names = ['egon','alex_sb','wupeiqi','yuanhao']
res4 = (name.upper() for name in names)
print(list(res4))
res5 = (len(name) for name in names if name.endswith('sb'))
print(res5)
