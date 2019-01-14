# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:33:03 2019

@author: shkim
"""
#%%
from math import hypot

#%%
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    # 해당 클래스를 출력했을 때 형식을 결정함
    def __repr__(self):
        return 'Vecotr(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)  # euclidean norm, sqrt(x*x + y*y)
    
    # __bool__이 구현되어 있지 않으면 __len__을 호출하며, __len__도 미구현되었으면 True를 반환
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
#%%
if __name__ == "__main__":
    v1 = Vector(2, 1)
    print(v1)           # __repr__ called
    print(bool(v1))     # __bool__ called    


#%%
    v1 = Vector(2,1)
    v2 = Vector(2,4)
    print(v1+v2)
    print(abs(v1), abs(v2), abs(v1+v2))
    print(v1*3)
    
#%%
    """
    <참고> __str__ 과 __repr__ 의 차이
    %r calls repr, while %s calls str. 
    These may behave differently for some types, but not for others: 
    repr returns "a printable representation of an object", 
    while str returns "a nicely printable representation of an object". 
    For example, they are different for strings:
    둘 중 하나만 구현해야 한다면 __repr__ 구현을 권장함. 
    __str__ 메서드가 구현되어 있지 않을 때 __repr__ 를 호출하기 때문임.
    """
    s = 'spam'
    print(repr(s))
    print(str(s))
 
        
#%%
    """
    Vector.__bool__()의 Optimization 버전
    def __abs__(self):
    eturn bool(self.x or self.y)  
    """
    