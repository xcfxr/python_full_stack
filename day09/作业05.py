res = {'k1': [], 'k2': []}
for each in [11,22,33,44,55,66,77,88,99,90]:
    if each > 66:
        res['k1'].append(each)
    elif each < 66:
        res['k2'].append(each)