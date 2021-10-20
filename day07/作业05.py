count = 1
sum = 0
while count < 100:
    if count % 2 == 1:
        sum += count
    else:
        sum -= count
    count += 1
print(sum)