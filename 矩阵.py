#coding=utf-8
#qpy:console
#qpy:2

import numpy as np

#向量点乘
mat=np.matrix('1 2 3')  #定义矩阵
dot=np.array([3,2,1])   #权重/向量
print np.dot(mat,dot)  #矩阵乘法
#[[10]]

#矩阵乘向量
mat=np.matrix('1 2')
dot=np.array([[1,2],[2,3]])
print np.dot(mat,dot)
#5,8

#向量乘矩阵
mat=np.matrix('1 2;3 2')
dot=np.array([1,2])
print np.dot(mat,dot)
#5,8

#矩阵乘矩阵
mat=np.mat('1 2;3 4')
dot=np.array([[0,1],[1,2]])
print np.dot(mat,dot)
#2 4,5 11
