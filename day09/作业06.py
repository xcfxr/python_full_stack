s='hello alex alex say hello sb sb'
words = s.split()
fre = {}
for word in words:
    if fre.get(word):
        fre[word] += 1
    else:
        fre[word] = 1
print(fre)