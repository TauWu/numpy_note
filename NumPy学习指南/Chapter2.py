# -*- coding: utf-8 -*-

from numpy import *

# 生成一个0-4的数组对象
a = arange(5)
print(a)
print(a.dtype)
print(a.shape)      # 返回每个维度的长度 【1*5】

# 创建二维数组
m = array([arange(3), arange(3), arange(3), [1,1,4]])
print(m)
print(m.shape)      # 返回每个维度的长度 【4*3】

print(m[3])         # 取值类似Python里的List
print(m[3,1:])

# 创建三维数组
t = arange(24).reshape(2, 3, 4) # 创建一个一维数组后将它重构成三维的
print(t.shape)
print(t)
print(t[0,:,0])
print(t[1,...])

# 数组的展开
print(t[...,0:1])
print(t[...,0:1].ravel())