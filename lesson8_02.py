#! python 3.10
'''
py 文件說明
'''

import math 
# 1 ~ 100 質數
def checkPrime(start:int, end:int) -> tuple:
    '''
    check 是否質數
    '''
    Tu = []
    for i in range(start, end+1):
        if i <= 1:
            continue
        
        isPrime = True
        for j in range(2, math.floor(math.pow(i, 0.5))+1):
            if(i%j == 0):
                isPrime = False
                break;
        if isPrime:
            Tu.append(i)
    return tuple(Tu)           

result = checkPrime(1, 50)
print(result)


#help(checkPrime)