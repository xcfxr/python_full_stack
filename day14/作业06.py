def check_dict(dic):
    for k,v  in dic.items():
        if len(v) > 2:
            dic[k] = v[:2]