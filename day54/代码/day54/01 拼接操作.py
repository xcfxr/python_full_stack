# l = [1,2,3,4,5,6,7]
# res = '|'.join(l)
# print(res)

# map  映射
# l = [1,2,3,4,5]
# res = map(lambda x:x**2,l)
# print(list(res))


# zip  拉链
# l1 = [111,222,333,444,555]
# l2 = ['贤妻','浏阳','小张']
# l3 = [1,2,3,4,5,6,7,8,]
# res = zip(l1,l2,l3)  # 以最短的为主
# print(list(res))


# filter  过滤
# l = [1,2,3,4,5,6,7,8]
# res = filter(lambda x:x>3,l)
# print(list(res))  # [4, 5, 6, 7, 8]



# reduce  多个进一个出
# from functools import reduce
# l = [1,2,3,4,5,6]
# # res = reduce(lambda x,y:x+y,l)
# res = reduce(lambda x,y:x+y,l,100)
# print(res)


import json
json.JSONEncoder








