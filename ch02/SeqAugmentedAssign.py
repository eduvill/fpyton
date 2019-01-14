# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:26:37 2019

@author: shkim
"""

#%%
# Augmented Assignment with Sequences
# 시퀀스의 복합할당 
"""
o +=과 *= 등의 복합 할당 연산자는 첫 번째 피연산자에 따라 상당히 다르게 작동함
o += 연산자가 작동하도록 만드는 특수 메서드는 __iadd__()임
 __iadd__() 메서드가 구현되어 있지 않으면 파이썬은 대신 __add__() 메서드를 호출함
o *= 연산자의 경우에는 __imul__() 메서드를 통해 구현됨
o a += b  연산의 처리
 a가 __iadd__() 메서드를 구현하면 구현된 메서드가 호출됨
 a가 list, bytearray, array.array 등 가변 시퀀스인 경우 a의 값이 변경됨
 a가 __iadd__() 메서드를 구현하지 않은 경우 a += b 표현식은 a = a + b가 되어 먼저 a + b 를 평가하고 객체를 새로 생성한 후 a에 할당됨
 즉, __iadd__() 메서드 구현 여부에 따라 a변수가 가리키는 객체의 정체성이 달라짐
o 일반적으로 가변 시퀀스에 대해서는 __iadd__() 메서드를 구현해서  += 연산자가 기존 객체의 내용을 변경하게 만드는 것이 좋음
 불변 시퀀스는 이 연산을 수행할 수 없음
"""

l = [1, 2, 3]
print(id(l))

l *= 2
print(id(l))


t = (1, 2, 3)
print(id(t))

t *= 2
print(id(t))


#%%
# 다음 표현식을 평가한 결과는 무엇일까?

t = (1, 2, [30, 40])
t[2] += [50, 60]

"""
a. (1, 2, [30, 40, 50, 60])
b. TypeError 발생
c. a,b 모두 틀림
d. a,b 둘다 맞음
"""


#%%
# 다음 표현식을 평가한 결과는 무엇일까?

t = (1, 2, [30, 40])
print(id(t), id(t[0]), id(t[1]), id(t[2]))
print(id(t), id(t[2]))

t[2] += [50, 60]  # TypeError 발생, but 값은 변경되어 있음
#t
#id(t), id(t[2])

t[2].extend([50, 60])  # ok!!
print(t)


#t[0] += 10  # TypeError 발생 & 값 변경 안됨
#t

#t = (1, 2, 3)
#print(id(t), id(t[0]), id(t[1]), id(t[2]))

#%%
# 복합 할당 표현식에 대한 바이트 코드 살펴보기
import dis
dis.dis('s[a] += b')

#%%
import dis
dis.dis('t = (1, 2, [30, 40])')

#%%