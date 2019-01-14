# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:26:37 2019

@author: shkim
"""
#%%
# Sequence 대체 기법
# - 덱 및 기타 큐 
"""
append()와 pop() 메서드를 사용해서 리스트를 스택이나 큐로 사용할 수 있음
그러나 리스트 왼쪽(0번 인덱스)에 삽입하거나 삭제하는 연산은
 전체 리스트를 이동시켜야 하므로 처리 부담이 큼
덱(collections.deque) 클래스
- 큐의 양쪽 어디에서든 빠르게 삽입 및 삭제할 수 있도록 설계된 thread-safe 양방향큐임
- '최근에 본 항목'이나 이와 비슷한 것들의 목록을 유지할 때도 사용할 수 있음 
- 최대 길이를 설정해서 제한된 항목만 유지할 수도 있으므로 
  덱이 꽉찬 후에는 새로운 항목을 추가할 때 반대쪽 항목을 버림
"""

# 덱 이용하기 
from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate()
print(dq)
dq.rotate(2)
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11,12,13])
print(dq)

dq.extendleft([10,20,30,40])
print(dq)

#%%