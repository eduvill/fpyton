# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:26:37 2019

@author: shkim
"""
#%%
# Sequence 대체 기법
# - 배열
"""
커다란 실수 배열의 생성, 저장, 로딩
- fromfile() : float() 내장함수를 이용해 텍스트파일에서 파싱하면서 숫자를 읽어오는 것보다 60배가랼 빠름
- tofile() : 각 행마다 실수 하나씩 파일에 저장하는 것보다 7배 가랼 빠름
- 배밀도 실수 천만개 저장 이진 파일 크기 : 80,000,000바이트(배밀도 실수 한개 8바이트)
- 배밀도 실수 천만개 저장시 tofile() 이용 : 181,515,739바이트 
"""
from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(len(floats))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(len(floats2))
print(floats2[-1])

#%%
# 배열의 정렬
"""
배열의 정렬
- 파이썬 3.5까지 array 형은 list.sort() 처럼 배열을 직접 변경하는 메서드가 없음
- 배열을 정렬하려면 sorted() 함수를 호출하여 다시 배열을 만들어야 함
"""

from array import array
from random import random

floats = array('d', (random() for i in range(10**1)))
print(floats)

#print(floats.sort())  # error
s_floats = array(floats.typecode, sorted(floats))
print(s_floats)

#%%
"""
객체 직렬화
- pickle 모듈도 숫자 데이터를 빠르고 융통성 있게 저장할 수 있음
- http://bit.ly/py-pickle
pickle.dump()
- 실수 배열을 array.tofile() 메서드 만큼 빠르게 저장함
- 복소수, 내포된 컬렉션, 사용자정의 객체 등 거의 모든 내장 자료형 처리 가능함 
"""

"""
레스터 이미지(raster images) 처럼 이진 데이터를 표현하는 숫자 배열을 위하여
파이썬은 bytes와 bytearray 형을 제공함
"""
