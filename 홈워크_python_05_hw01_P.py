# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
from calendar import *
import calendar
week_list = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

def time(year):
    if calendar.isleap(year) == 1:
        return("윤년입니다. 연도를 다시 입력해주세요")
    else:
        print(calendar(year))
        month = int(input())
        day = int(input())
        if week_list[calendar.weekday(year,month,day)] == "월요일":
            print("경고 월요일입니다.")
            return("{'년' :" ,year, "'월':",month, "'일':", day, "'요일:", week_list[calendar.weekday(year,month,day)])
        else:
            return("{'년' :" ,year, "'월':",month, "'일':", day, "'요일:", week_list[calendar.weekday(year,month,day)])        
        