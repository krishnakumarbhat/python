# from this import d
# from django.template import base
from matplotlib.pyplot import axis
import numpy as np

a=np.array([1,2,3])
b=np.array([[5,2,7],[4,5,6]])
print(a,b)
print(a.ndim)
print(b.ndim)
print(type(a),type(b))

# np.linspace()
arr1  = np.arange(0,10,2,dtype="int")
print(arr1)
arr = np.linspace(0,10,5,endpoint=True,retstep=True,dtype="int")
print(arr)
arr23 = np.logspace(0,10,5,endpoint=False,base=2,dtype="int")
print(arr23)

res = np.asarray(b,dtype="int",order="f")

print(res)

res1 = np.asarray(b,dtype="int",order="c")
for i in np.nditer(res1):
    print(i)
s= b"helo"
c= np.frombuffer(s,dtype="int",count=-1,offset=0)
print(c)

list1 = [1,2,4,6,7]

d= np.fromiter(list1,dtype="float",count=3)
print(d)

as1 = np.shape(b)
print(as1)
as2 = np.reshape(a,(3,1))
print(as2)


as3 = np.zeros((4,4),dtype="int")
print(as3)

as4 = np.ones((4,4),dtype="int")
print(as4)

as5 = np.full((4,4),100,dtype="int")
print(as5)

as6 = np.eye(43,dtype="int")
print(as6)

# acessing array for 2d here and for 3D it's like this b[1,2,4]
print(b[1,2])

#slicijng in 2D
print(b[0:2,0:2])


#axis attributes
asc0 = np.sort(b,axis = 0)
print(asc0)

asc0 = np.sort(b,axis = 1)
print(asc0)

#data type

print(b.dtype)
# here i canged the datatype to u
csd = b.astype("U")
print(csd)
#this wiil not change origenal
cpo = b.copy()
#this wiil not change origenal
vie = b.view()
print(cpo.base)
print(vie.base)


#joining

jot = np.arange(6).reshape(2,3)
jot2 = np.arange(7,13).reshape(2,3)
print(jot)
print(jot2)
#you have to pu two brackket *imp 
cdf =np.concatenate((jot,jot2))
cdf2 =(np.concatenate((jot,jot2),axis=1))
print(cdf ,cdf2)

print(np.stack((jot,jot2)))
print(np.vstack((jot,jot2)))
print(np.hstack((jot,jot2)))
print(np.dstack((jot,jot2)))


print(np.split(jot,2))
print(np.array_split(jot,2))
print(np.vsplit(b,1))
print(np.hsplit(b,1))


print("oinn")
print(np.where(a==2))
print(np.where(a%2 ==0))
print(np.searchsorted(a,2.5))

'''sorting using axis 
'''

np.sort(a)
print(np.sort(b,axis = 0))
print(np.sort(b,axis = 1,))

dso = np.dtype([('name','SlO'),('perc',float)])
stud = np.array([("abc",90.3),("def",95.3),("ghi",65.4)])
print(stud)






