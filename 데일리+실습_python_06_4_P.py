entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

entry_set = set(entry_record) # 만들 딕셔너리에 키 값을 넣기 위하여 중복 제거

entry = {} # 누가 몇번 들어 왔는지 출입 기록을 보여줄 리스트 생성
 
for i in entry_set: # entry 딕셔너리에 키 값을 하나씩 넣어주며 초기 값으로 0 할당
    entry[i] = 0

for i in entry_record:  # 출입 기록을 하나씩 넣으며 반복문 진행
    entry[i] += 1 # 키 값이 나올 때 마다 그 값에 1추가

entry = sorted(entry.items(), key=lambda x: x[1], reverse=True) # 출입 기록이 많은 순으로 정렬

print("입장이 가장 많은 Top3")
for i in range(3): # 출입기록이 가장 많은 3명 출력
    print(entry[i])
    
entry = dict(entry)
    
    
exit_set = set(exit_record) # 만들 딕셔너리에 키 값을 넣기 위하여 중복 제거
exit = {} # 누가 몇번 나갔는지 퇴장 기록을 보여주는 딕셔너리 생성

for i in exit_set: # 퇴장 기록을 보여주는 딕셔너리에 키 값 입력하고 값으로 0 할당
    exit[i] = 0
    
for i in exit_record: # 퇴장 기록이 보일 떄 마다 1씩 추가
    exit[i] += 1
    
exit = sorted(exit.items(), key=lambda x: x[1], reverse=True) # 퇴장 기록이 많은 순으로 정령

exit = dict(exit) # 딕셔너리 구조로 변환

answer = {} # 입장 기록과 퇴장기록의 차이를 보여주는 딕셔너리 생성

for i in entry.keys(): # 입장 기록의 키 를 넣으며 반목문 실행
    for j in exit.keys(): # 퇴장 기록의 키 를 넣으며 반복문 실행
        if i == j: # 만약 입장 기록과 퇴장 기록의 키 값이 같으면
            answer[i] = exit[j] - entry[i] # 차이를 보여주는 딕셔너리의 키를 추가하고 그의 값으로 퇴장기록의 수에서 입장기록의 수를 뺀 값을 할당
        else:
            continue
print("출입 기록이 수상한사람")       
for i in answer.keys(): # 차이의 딕셔너리의 키 값을 넣으며 반복문 진행
    if answer[i] > 0: # 값이 0보다 크다면
        print(i,"의 퇴장 기록이", answer[i],"회 더 많아 수상합니다.")
    elif answer[i] < 0: # 값이 0 보다 작다면
        print(i,"의 입장 기록이", abs(answer[i]),"회 더 많아 수상합니다.")
