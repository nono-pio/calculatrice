import numpy as np
import math

def rac(x, n = 1):
  sign = np.angle(x)
  x = np.abs(x)

  result = []

  for i in range(n):
    result.append(pow(x,1/n)*(np.cos(sign/n + 2*i* math.pi/n)+np.sin(sign/n + 2*i*math.pi/n)*1j))
  
  return np.around(result, 10)