import math
import sys
import random as rd
fd = open("./a.dat","w+")
M = 0
N = 0
if len(sys.argv) > 2:
   M = int(sys.argv[1])
   N = int(sys.argv[2])
i = 0
while i < M:
  j= 0
  while j < N:
    j += 1
    x = rd.random()
    fd.write("%.2f  " % math.log(x/(1-x)))
  i += 1
  fd.write("\r\n")
fd.close()

