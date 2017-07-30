'''
@author: mzanco
'''

import sys

if len(sys.argv) > 1 and sys.argv[1].isdecimal():
    n = int(sys.argv[1])
   
    beforeVal, nowVal, nextVal = 0, 1, 0
    
    while(n != 0):
        print(nowVal, ('', ', ')[n > 1], end='')
        nextVal = beforeVal + nowVal
        beforeVal = nowVal
        nowVal = nextVal
        n -= 1
else: 
    print('Invalid arguments')
