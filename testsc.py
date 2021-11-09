from multiprocessing import cpu_count
from multiprocessing import Pool
import numpy as np
import sys
import time 

def f(a):
    x = np.sum(np.arange(0, 1e7, 1)**10) * a
    return x*x

if __name__ == '__main__':
    core = cpu_count()
    print("cores = %d"%core)
    # print("version ", sys.version)

    a = range(1, 8 + 1)
    print(len(a))
    b1 = [];
    ta1 = time.time()
    for i in a:
        b1.append(f(i)) 
   
    tb1 = time.time()


    ta2 = time.time()
    with Pool() as pool2:
        b2 = pool2.map(f,a)
       
    tb2 = time.time()

    print(b1) 
    print("One core costs %4.2fs\n"%(tb1 - ta1))

    print(b2) 
    print("Multi cores cost %4.2fs\n"%(tb2 - ta2))

    with open("testsc.txt", 'w') as f:
        print("One core costs %4.2fs"%(tb1 - ta1), file = f)
        print("Multi cores cost %4.2fs"%(tb2 - ta2) , file = f)



