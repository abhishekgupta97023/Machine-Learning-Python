import numpy as np

a=np.array([[89,56.5,32],[34,0,56],[3,45,98]])
print(a)


##AXIS 0 DEFINES COLUMNS and axis 1 defines horizontal rows
b=a.sum(axis=0)
print(b)


##Percentage of each element with the sum of each column
print(100*a/b.reshape(1,3))


##Test
a = np.random.randn(2, 3) # a.shape = (2, 3)
b = np.random.randn(2, 1) # b.shape = (2, 1)
c = a + b

print(a,b,c)




