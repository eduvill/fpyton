# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:26:37 2019

@author: shkim
"""
#%%
# Sequence 대체 기법
# - NumPy와 SciPy
"""
NumPy와 SciPy
- 비표준 라이브러리임
- NumPy와 SciPy가 제공하는 고급 배열 및 행렬 연산 덕분에 
  파이썬 과학계산 애플리케이션에서 널리 사용되게 됨
- NumPy는 숫자뿐만 아니라 사용자 정의 레코드도 저장할 수 있는 
  다차원 동형 배열 및 행렬을 구현하고 요소 단위에서 효율적으로 연산할 수 있게 해줌
- SciPy는 NumPy를 기반으로 작성된 라이브러리로서, 
  선형대수학, 수치해석, 통계학에 나오는 여러 과학 계산 알고리즘을 제공함
- SciPy는 Netlib 리포지토리(http://www.netlib.org)가 제공하는 
  C 및 포트란 코드 기반을 활용함으로써 빠르고 신뢰성이 높음
- 따라서 SciPy는 C와 포트란에서 최적화되고 업계에서 입증된 수치계산 함수를 
  대화형 고급 파이썬 API를 통해 과학자들에게 제공함 
"""
# numpy.ndarray에서 행과 열을 이용한 기본 연산 
import numpy

a = numpy.arange(12)
print(a)
type(a)
print(a.shape)

a.shape = 3, 4
print(a)
type(a)
print(a.shape)

print(a[2])
print(a[2,1])

print(a[:,1])

print(a.transpose())

#%%
# numpy.ndarray의 모든 요소를 저장, 로딩, 처리하는 고급연산 지원
import numpy

floats = numpy.loadtxt('./floats.bin')


