import numpy as np
import time

a=np.array([1,2,3,4])
print(a)



a=np.random.rand(1000000)
b=np.random.rand(1000000)
tic=time.time()
c=np.dot(a,b)
toc=time.time()
print("Vectorized Time taken "+str(1000*(toc-tic))+" ms")
print(c)


##NON VECTORIZED
d=0
tic=time.time()
for i in range(1000000):
    d+=a[i]*b[i]
toc=time.time()
print("NonVectorized Time taken "+str(1000*(toc-tic))+" ms")  
print(d)

##Creates a matrix of zeroes of 5*2 dimensions
u=np.zeros((5,2))
print(u)
