#!/usr/bin/env python
# coding: utf-8

# 달력출력에 필요한 함수

# In[27]:


# 연도를 인수로 넘겨받아 윤년, 평년을 판단하는 함수

def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# In[28]:


# 연, 월을 인수로 받아 그 달의 마지막 날짜를 리턴
# 12달의 마지막 날짜를 기억하는 리스트를 만든다.
# 윤년, 평년에 따른 2월의 마지막 날짜
# 마지막 날짜를 리턴

def lastDay(year, month):
    last = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    last[1] = 29 if month == 2 and isLeapYear(year) else 28
    return last[month - 1]


# In[37]:


# 연, 월, 일을 인수로 받아 1년 1월 1일 부터 지나온 날짜의 함계를 리턴하는 함수
'''
def totalDay(year, month, day):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 365 * (year - 1) + day
    
    for i in range(1, year, 1):
        if i % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            total += 1
    
    for i in range(month - 1):
        total += days[i]
    
    return total
'''


# In[42]:


# 연, 월, 일을 인수로 받아 1년 1월 1일 부터 지나온 날짜의 함계를 리턴하는 함수
# 선생님 버전

def totalDay(year, month, day):
    total = 365 * (year - 1) + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400 # 윤년 더하기
        
    # 전년도 12월 31일 까지 지난 날짜에 전달 까지 지난 날짜를 더하기
    for i in range(1, month):
        total += lastDay(year, i)
    
    return total + day


# In[49]:


# 연, 월, 일을 인수로 넘겨받아 요일을 숫자로 리턴하는 함수
# 일요일(0), 월요일(1), ... ,토요일(6)

def weekDay(year, month, day):
    day = totalDay(year, month, day) % 7
    
    return day


# In[50]:


if __name__ == "__main__":
    print(isLeapYear(2000))
    print(lastDay(2000, 2))
    print(totalDay(2020, 6, 15))
    print(weekDay(2020, 6, 15))

