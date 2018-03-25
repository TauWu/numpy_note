# -*- coding: utf-8 -*-

import numpy as np

i2 = np.eye(2)      # 生成一个单位矩阵
print(i2)
i = i2.real.astype(int)
np.savetxt('eye.log', i)

c, v = np.loadtxt('data.csv', delimiter=',', usecols=(1,3), unpack=True)

print(c)
print(v)