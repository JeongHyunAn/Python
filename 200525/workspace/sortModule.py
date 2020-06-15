#!/usr/bin/env python
# coding: utf-8

# module을 만들시에 파일명이 숫자로 시작 할 수 없다.  
# 선택 정렬(selection sort)은 특정 위치의 값을 선택해서 나머지 값과 비교하여 정렬

# In[37]:


# 오름차순 정렬함수
def selectionSortAsc(data):
    for i in range(0, len(data)-1, 1):
        for j in range(i+1, len(data), 1):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data;

# 내림차순 정렬함수
def selectionSortDesc(data):
    for i in range(0, len(data)-1, 1):
        for j in range(i+1, len(data), 1):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
    return data;

