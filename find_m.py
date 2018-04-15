fd = open("./a.dat","r")
line = fd.readline()
N = 2
bl = 0
while len(line)>0 :
  ver = line.split()
  if len(ver) > N :
    if bl == 1 :
      print ",",
    else:
      bl = 1
    print ver[N-1],
  line = fd.readline()
