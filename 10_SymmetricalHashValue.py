import hashlib

import random

import os

#字母表，用于生成message
seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
count=0

#判断字符串是否对称
def reverce(str):
    if list(str)==list(reversed(str)):
        return True
    else:
        return False

while True:
    #随机生成64Byte的Message
    random_massage=''
    for i in range(64):
        random_massage=random_massage+random.choice(seed)
    #print(random_massage)

    #进行MD5加密
    result=(hashlib.md5(random_massage.encode())).hexdigest()
    #print(result)

    #检查128bit Hash值是否对称
    judge=reverce(result)
    if judge==True :
        print(judge)
        print('message:',random_massage)
        print(result)
        break
    else:
         if count%100000==0:
            print(judge)
            print('message:',random_massage)
            print(result)


    count=count+1

    