import sys
N = 0
if len(sys.argv) > 1 :
  N = int(sys.argv[1])
if N <= 0:
  sys.exit(1)
fd = open("./a.dat","r")
line = fd.readline()
bl = 0
while len(line)>0 :
  ver = line.split()
  if len(ver) >= N :
    if bl == 1 :
      print ",",
    else:
      bl = 1
    print ver[N-1],
  line = fd.readline()
