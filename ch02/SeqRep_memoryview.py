# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:26:37 2019

@author: shkim
"""
#%%
# Sequence 대체 기법
# - 메모리 뷰 (memoryview)
"""
메모리 뷰 (memoryview)
- memoryview 내장 클래스는 공유 메모리 시퀀스형으로서 
  bytes를 복사하지 않고 배열의 슬라이스를 다룰 수 있게 해줌
- 이 클래스는 NumPy 라이브러리에서 영감을 받아 만들어짐 
- http://bit.ly/1Vm6C8B
  메모리 뷰는 본질적으로 파이썬 자체에 들어 있는 NumPy 배열 구조체를 일반화한 것임
  메모리 뷰는 PIL 이미지, SQLite 데이터베이스, NumPy 배열 등 
  데이터 구조체를 복사하지 않고 메모리를 공유할 수 있도록 해줌
  데이터 셋이 커지는 경우에 아주 중요한 기법
- array 모듈과 비슷한 표기법을 사용하는 memoryview.cast() 메서드는
  바이트를 이동시키지 않고 C언어의 형변환 연산자처럼 여러 바이트로된 데이터를 
  읽거나 쓰는 방식을 바꿀 수 있게 해줌
- memoryview.cast()는 또다른 memoryview 객체를 반환하며 언제나 동일한 메모리를 공유
"""
from array import array

numbers = array('h', [-2,-1,0,1,2])  # h : short int
memv = memoryview(numbers)

print(len(memv), memv)
print(memv[0])

memv_oct = memv.cast('B')  # unsigned char
print(len(memv_oct), memv_oct)
print(memv_oct[0])

print(memv_oct.tolist())

memv_oct[5] = 4
print(memv_oct.tolist())
print(memv.tolist())

#%%