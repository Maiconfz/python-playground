'''
@author: mzanco
'''

a = [1, 2, 3, 4, 5]

print('"a" list: ', a)

while(a[-1] != 10):
    a.append(a[-1] + 1)
    
print('new "a" list: ', a)
    
