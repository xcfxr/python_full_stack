import configparser
config = configparser.ConfigParser()
# config['MYSQL'] = {
#     'HOST' : '127.0.0.1',
#     'PORT' : '3306',
#     'USER' : 'tank',
#     'PASSWORD': '123456',
# }
# with open('mysql.ini', 'w') as f:
#     config.write(f)
config.read('./mysql.ini')
print(config.sections())
for each in config.sections():
    print(config.options(each))
    print(config.items(each))
print(config.get('MYSQL', 'host'))
print(config['MYSQL']['USER'])