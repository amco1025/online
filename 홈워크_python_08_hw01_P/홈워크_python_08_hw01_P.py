# 입력 예시
class Point:  # 주어지는 좌표 입력
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Rectangle: # 주어진 2개의 좌표를 하나의 self에 저장
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
        
    
    def get_area(self): # 넓이 구하기
        return abs(self.p1.x-self.p2.x) * abs(self.p1.y - self.p2.y)
    
    def get_perimeter(self): # 둘레길이 구하기
        return 2*(abs(self.p2.x-self.p1.x) + abs(self.p2.y - self.p1.y))
    
    def is_square(self): # 정사각형 유무 확인
        if abs(self.p2.x-self.p1.x) == abs(self.p2.y - self.p1.y):
            return True
        else:
            return False


 

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

# p3 = Point(3, 7)
# p4 = Point(6, 4)
# r2 = Rectangle(p3, p4)
# print(r2.get_area())
# print(r2.get_perimeter())
# print(r2.is_square())

# # 출력 예시
# # 4
# 8
# True

# 9
# 12
# True