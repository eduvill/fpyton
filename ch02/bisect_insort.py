# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:26:37 2019

@author: shkim
"""
#%%
# 정렬된 시퀀스를 bisect로 관리하기
"""
bisect 모듈은 bisect()와 insort() 함수를 제공함
bisect()는 이진 검색 알고리즘을 이용해서 시퀀스를 검색함
insort()는 정렬된 시퀀스 안에 항목을 삽입함
"""
# bisect.insert()로 삽입하기
# - 정렬은 값비싼 연산이므로 시퀀스를 일단 정렬한 후에는 정렬 상태를 유지하는 것이 좋음
# - 그렇기 때문에 bisect.insort() 함수가 만들어짐
# - insort(seq, item)은 seq를 오름차순으로 유지한 채로 item을 seq에 삽입
# - insert_left() : 삽입위치 검색 시 bisect_left() 사용

import bisect
import random

SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
    

#%%