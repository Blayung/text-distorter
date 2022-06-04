#!/bin/python3
from random import randint, choice

text=input("Type in text > ")
try:
    distortion=int(input("Type in level of distortion (0-100) > "))
    if distortion<0 or distortion>100:
        print("Level of distortion must be between 0 and 100!")
        exit()
except:
    print("Level of distortion has to be number!")
    exit()
text2=list(text)

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

idx=0
for _ in text2:
    if randint(0,100)<distortion:
        if randint(0,1)==1:
            del text2[idx]
        else:
            text2[idx]=choice(alphabet)
    idx+=1

idx=0
for _ in text2:
    if randint(0,100)<distortion:
        if text2[idx].isupper():
            text2[idx]=text2[idx].lower()
        elif text2[idx].islower():
            text2[idx]=text2[idx].upper()
    idx+=1

text3=""
for x in text2:
    text3+=x

print(text3)
