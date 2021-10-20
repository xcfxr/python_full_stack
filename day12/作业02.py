# with open('aaa.txt', 'r+', encoding='utf-8') as f:
#     f.write('h')
# with open('aaa.txt', 'rb+') as f:
#     f.seek(-8, 2)
#     print(f.read().decode('utf-8'))
# with open('aaa.txt', 'r+', encoding='utf-8') as f:
#     f.seek(2, 0)
#     print(f.read(6)) #t模式下读取字符可以超出，默认到尾
# ## t模式只能从前往后seek

with open('aaa.txt', 'a', encoding='utf-8') as f:
    f.seek(1, 0) ## a模式下写 seek没有用
    f.write('坏')
'''
【r】解读：必须有文件，从最开始读
【r+】解读：必须有文件，从最开始读，从最开始写(覆盖写)
【w】解读：无文件创建，从最开始写(清空写)
【w+】解读：无文件创建，从最开始写(清空写)，读不到内容(因为w先清空内容了)
【a】解读：无文件创建，从末尾写(追加写)
【a+】解读：无文件创建，从末尾写(追加写)，读不到内容(因为光标在末尾，可用seek移动光标)
'''