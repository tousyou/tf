import math
import random as rd
fd = open("./a.dat","w+")
i = 0
M = 10
N = 11
while i < M:
  j= 0
  while j < N:
    j += 1
    x = rd.random()
    fd.write("%.2f  " % math.log(x/(1-x)))
  i += 1
  fd.write("\r\n")
fd.close()
