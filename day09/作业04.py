msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
buy_list = []
while True:
    for key, value in msg_dic.items():
        print('商品名称:[%s] 单价:[%s]元' % (key, value))
    shop_name = input('请输入要购买的商品').strip()
    if shop_name not in msg_dic:
        print('输入有误， 请输入存在的商品')
    else:
        amount = input('请输入购买的数量')
        if amount.isdigit():
            amount = int(amount)
            shop_tuple = (shop_name, amount * msg_dic[shop_name], amount)
            buy_list.append(shop_tuple)
        else:
            print('请输入数字')
