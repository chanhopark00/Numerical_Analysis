import numpy as np
def jacobi(v):
  tmp = np.array([-1.0,2.0,3.0])
  r = np.array([0,-2.0,3.0,-3.0,0,1.0,2.0,-2.0,0])
  r = r.reshape((3,3)).copy()
  v = tmp - np.dot(r,v)

  out = np.array([0.0,0.0,0.0])
  out[0] = v[0]/5
  out[1] = v[1]/9
  out[2] = -v[2]/7
  
  return out

def gauss(v):
  tmp = np.array([-1.0,2.0,3.0])
  r = np.array([0,-2.0,3.0,0,0,1.0,0,0,0])
  r = r.reshape((3,3)).copy()
  v = tmp - np.dot(r,v)
  l = np.array([0.2,0.0,0.0,0.066666,0.111111,0.0,0.0380952, -0.031746, -0.142857])
  l = l.reshape((3,3)).copy() 
  v = np.dot(l,v)
  return v

v = np.array([0,0,0])
n = 1
while(n < 11):
  print(jacobi(v))
  v = jacobi(v)
  n = n + 1

print("___________________")
v = np.array([0,0,0])
n = 1
while(n < 11):
  print(gauss(v))
  v = gauss(v)
  n = n + 1
