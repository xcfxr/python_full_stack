l=['a','b',1,'a','a']
print(set(l))
new_l = []
for each in l:
    if each not in new_l:
        new_l.append(each)
print(new_l)
'''
f = open('', 'rt')
lines = []
for line in f:
    if line not in lines:
        lines.append(line)
print(lines)

'''
l=[
    {'name':'egon','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'egon','age':20,'sex':'female'},
    {'name':'egon','age':18,'sex':'male'},
    {'name':'egon','age':18,'sex':'male'},
]
new_l = []
for each in l:
    if each not in new_l:
        new_l.append(each)
print(new_l)
