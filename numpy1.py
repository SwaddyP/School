import numpy as np
mylist=[1,2,3]
x=np.array(mylist)
print(x)
y = np.array([4,5,6])
print(y)
m = np.array(([7,8,9],[10,11,12]))
print(m)
print(m.shape)
n = np.arrange(0,30,2)
print(n)
n=n.reshape(3,5)
print(n)
o=np.linespace(0,4,9)
print(o)
o.resize(3,3)
print(o)
print(np.ones((3,2)))
print(np.zeroes(2,3))
print(np.eye(3))
print(np.diag(y))
print(np.array[1,2,3]*3)
print(np.repeat([1,2,3],3))
print(np.vstack([p,2*p]))
print(np.hstack([p,2*p]))
print(x.dot(y))
z=np.array([y,y**2])
print(z.shape)
print(z.dtype)
z=z.astype('f')
print(z.dtype)
print(z.T.shape)
a = np.array([-4,4,1,2,3])
print(a.sum())
print(a.min())
print(a.max())
print(a.std())
print(a.mean())
print(a.argmax())
print(a.argmin())
s=np.arrange(13)**2
print(s)
test = np.random.randint(0,10,(4,3))
print(test)
for row in test:
    print(row)
for i in range(len(test)):
    print(test[i])
for i,row in enumerate(test):
    print('row',i,'is',row)