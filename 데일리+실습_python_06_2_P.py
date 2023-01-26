grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
big = 0
for i in grain_lst:
    if big < i[1]:
        big = i[1]
    else:
        continue
    
for i in grain_lst:
    if i[1] == big:
        print(i[0])
    else:
        continue
