#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random
num=random.randint(1,10)
print(num)
for i in range(1,4):
    a = int(input("请输入数字猜大小"))
    if a==num:
        print("恭喜猜对了")
        exit()
    elif a<num:
        print("小了")
    elif a>num:
        print("大了")

