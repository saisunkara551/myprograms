import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
for i in range(1,b+1):
	#print(a,'X',i,'=',a*i)
	print("%dX%d=%d"%(a,i,a*i))
