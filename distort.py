#!/bin/python3
from random import uniform, randint, choice
from sys import argv

try:
    distortion = float(argv[1])
    if distortion < 0 or distortion > 100:
        raise Exception()
    text=list(' '.join(argv[2:]))
except:
    print("Usage: python distort.py <0-100> <some text>")
    exit()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

i=0
for _ in text:
    if uniform(0,100) < distortion:
        if randint(0,1) == 1:
            del text[i]
        else:
            text[i] = choice(alphabet)
    i+=1

i=0
for _ in text:
    if uniform(0,100) < distortion:
        if text[i].isupper():
            text[i] = text[i].lower()
        elif text[i].islower():
            text[i] = text[i].upper()
    i+=1

print(''.join(text))
