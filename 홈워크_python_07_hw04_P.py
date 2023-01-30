# collatz(6)  # => 8
# collatz(16)  # => 4
# collatz(27)  # => 111
# collatz(626331)  # => -1

def collatz(num): # 함수 정의
    count = 0 # 반복 횟수를 나타내는 변수 설정 후 0 할당
    while num > 1: # 수가 1보다 큰 동안 반복 진행
        if num % 2 == 0: # 짝수라면
            num = num / 2
                
        elif num % 2 ==1: # 홀수라면
            num = (num*3) + 1
        count += 1 # 조건에 맞게 진행하며 진행할 때 마다 count값을 1씩증가
            
    if count > 500: # 반복이 끝났을 떄 count 가 500보다 크면 -1 출력 아니라면 반복횟수 출력
        count = -1
            
    print(count)
    
