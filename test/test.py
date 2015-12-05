
#import sys

#print sys.stdin.readlines()

import os

x0 = float(os.environ.get("X0",1.))
M = int(os.environ.get("M",20))



x = lambda n: x0 if n < 2 else 1. + 1./(x(n-1)+1) 


if __name__ == "__main__":
    for m in range(M):
        print "x("+str(m)+") = ", x(m)


