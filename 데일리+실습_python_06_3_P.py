# count_vowels('apple') #=> 2
# count_vowels('banana') #=> 3

def count_vowels(word): # 모음의 갯수를 반환해주는 함수 선언
    cnt = 0 # 모음의 개수를 나타내주는 변수로 초기값 0 할당
    for i in word: # i에 입력된 단어의 알파벳 하나씩 넣으며 반복문 실행
        if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]: # 만약 i가 모음이라면 cnt에 1을 더함
            cnt += 1
        else: # 아니라면 계속 반복문 진행
            continue
    
    print(cnt) # 모음의 갯수 출력

count_vowels('apple')