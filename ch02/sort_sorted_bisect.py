# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:26:37 2019

@author: shkim
"""

#%%
# list.sort()와 sorted() 내장 함수
"""
list.sort() 메서드는 사본을 만들지 않고 리스트 내부를 변경해서 정렬함
sort() 메서드는 타깃 객체를 변경하고 새로운 리스트를 생성하지 않았음을 알려주기 위하여 None을 반환함
이것은 파이썬 API의 중요한 관례임
객체를 직접 변경하는 함수나 메서드는 객체가 변경되었고 새로운 객체가 생성되지 않았음을 호출자에게 알려주기 위해 None을 반환해야 함
random.shuffle() 함수도 이와 동일하게 작동함
sorted() 내장 함수는 새로운 리스트를 생성해서 반환함
사실 sorted() 함수는 불변 시퀀스 및 제너레이터를 포함해서 반복 가능한 모든 객체를 인수로 받을 수 있음 
입력 받은 반복 가능한 객체의 자료형과 무관하게 sorted() 함수는 언제나 새로 생성한 리스트를 반환함
list.sort() 메서드와 sorted() 함수 모두 선택적으로 두 개의 키워드를 인수로 받음
reverse
key : min(), max(), itertools.groupby(), heapq.nlargest() 와 함께 사용
"""

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(fruits)
print(fruits.sort())
print(fruits)

#%%
# 정렬된 시퀀스를 bisect로 관리하기
"""
bisect 모듈은 bisect()와 insort() 함수를 제공함
bisect()는 이진 검색 알고리즘을 이용해서 시퀀스를 검색함
insort()는 정렬된 시퀀스 안에 항목을 삽입함
"""
# bisect()로 검색하기

import bisect
import sys

HAYSTACK = [1,4,5,6,8,12,15,20,21,23,23,26,29,30]
NEEDLES = [0,1,2,5,8,10,22,23,29,30,31]

ROW_FMT = '{0:2d} @ {1:2d}   {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    
    print('DEMO:', bisect_fn.__name__)
    print('haystack->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

#%%
# 시험점수를 입력 받아 등급 문자를 반환하는 grade() 함수
import bisect
import sys

def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33,99,77,70,89,90,100]])

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