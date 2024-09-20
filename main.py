import numpy as np

arr = np.array([1,2,3])
print(arr)
#Slicing in an array
arr = np.array([[-2,4,7],
                [-4,2,1],
                [7,5,3]])

sliced_arr=arr[:1,::2]
print(sliced_arr) 

print(np.array([1,2,3,4], dtype ='str'))

val = np.array([range(i,i+2) for i in [2,4,6]])
print(val)

#creat a 10-length integer array filled with zeros
op1 = np.zeros(10,dtype='int')
print(op1)
#create a 4x3 floating-point array filled with zeros
op2 = np.zeros((4,3),dtype='float')
print(op2)
#create a 3x2 string array filled with 1s
op3 = np.ones((3,2),dtype ='str')
print(op3)
#create a 2x3 array filled with 4.6
op3 = np.full((2,3),4.6)
print(op3)
#create an array filled with a linear sequence starting at 0, ending at 20, stepping by 3
op4 = np.arange(0,20,3)
print(op4)
#create an array of four values evenly spaced between 0 and 1
op5 = np.linspace(0,1,4)
print(op5)
#create a 3x3 array of uniformly distributed random values between 0 and 1
op6=np.random.random((3,3))
print(op6)
#create a 3x3 array of normally distributed random values with mean 0 and standard deviation
op7=np.random.normal(0,1,(3,3))
print(op7)
#create a 4x5 array using eye method/identity matrix
op8 = np.eye(4,5,dtype='float')
print(op8)
#create a 3x3 array of random integers
op9 = np.random.randint(0,10,(3,3))
print(op9)
#arithmatic
op10 = np.arange(4)
print(op10+5)
print(op10-5)
print(op10*2)
print(op10/2)
print(op10//2)
print(op10**2)
print(op10%2)
#Matrix manipulation
mat1 = np.array([[1,2],[4,5]])
mat2 = np.array([[7,8],[9,10]])
print(np.add(mat1,mat2))
print(np.subtract(mat1,mat2))
print(np.divide(mat1,mat2))
print(np.multiply(mat1,mat2))
print(np.dot(mat1,mat2))
print(np.sqrt(mat1))
print(np.sum(mat2))
print(np.sum(mat2,axis=0)) #column wise summation
print(np.sum(mat2,axis=1)) #row wise summation
#transpose matrix
print(mat1.T)
#Reshaping in numpy
# 1-D to 2-D
r = np.array([1,5,6,3,9,8,0,4,2,7])
n = r.size
row = 5
col = n//row
re1 = r.reshape((row,col))
print(re1)
re2 = np.reshape(r,(2,5))
print(re2)
# 1-D to 3-D
r = np.array([3,4,5,2,1,9,0,14,54,77,3,7,6,6,8,0,4,3,4,1])
re3 = r.reshape((2,2,5))
print(re3)
grid = np.arange(1,10,1).reshape(3,3)
print(grid)
#broadcasting
br1 = np.arange(3)+5
print(br1)
br2 = np.ones((3,3))+np.arange(3)
print(br2)
br3 = np.arange(3).reshape((3,1))+np.arange(3)
print(br3)
#estimation
sequence = [2,3,5,6,7,9]
variance = np.var(sequence)
print(variance)
stde = np.std(sequence)
print(stde)
#Comparison operators
cmp = np.array([1,2,3,4,5])
print(cmp<2)
print(cmp>2)
print(cmp<=2)
print(cmp>=2)
print(cmp!=2)
print(cmp==3)
#rng = np.random.RandomState(seed = 0)
x = np.random.randint(10,size=(3,4))
print(x<7)
