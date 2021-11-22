with open('a.txt', 'rt', encoding='utf-8') as f:
    long_line = len(max(f, key=lambda x: len(x)))
    print(long_line)
    g = (len(line) for line in f)
    print(sum(g))  ## 0

with open('a.txt', 'rt', encoding='utf-8') as f:
    g = (len(line) for line in f)
    print(sum(g))  ## 如果顶行写会报错，因为f已经close了

with open('shopping.txt', 'rt', encoding='utf-8') as f:
    items_info = []
    for line in f:
        item, price, amount = line.strip().split(',')
        items_info.append({'name': item, 'price': int(price), 'count': int(amount)})
    print(sum(item['price'] * item['count'] for item in items_info))
    g = (item for item in items_info if item['price'] > 10000)
    print(list(g))

'''
10、思考：判断下述说法是否正确
    题目1：
    1、应该将程序所有功能都扔到一个模块中，然后通过导入模块的方式引用它们 错误
    2、应该只将程序各部分组件共享的那一部分功能扔到一个模块中，然后通过导入模块的方式引用它们 错误
    
    题目2：
    运行python文件与导入python文件的区别是什么？ 导入会产生一个名称空间，然后在全局产生一个变量指向他
    运行的python文件产生的名称空间何时回收，为什么？  # 程序运行结束
    导入的python文件产生的名称空间何时回收，为什么？  #没有变量指向他时
'''