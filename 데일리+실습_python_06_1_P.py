# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

def de_identify(id):
    answer = ""
    for i in id:
        if len(answer) <= 5:
            answer = answer + i
        elif 5 < len(answer) <= 12:
            answer = answer + "*"
            
    return answer

print(de_identify('970103-1234567'))


# B. 출력예시
# 970103*******
# 861123******* 
