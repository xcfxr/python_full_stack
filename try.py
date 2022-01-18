import simplejson
obj = {'abc':123}
with open('./test.json', 'w') as fp:
    simplejson.dump(obj, fp)