#!/usr/bin/python3

def uppercase(str):
    if len(str) == 0:
        print("{}".format("\n"), end="")
    for i in range(len(str)):
        print("{}".format((chr(ord(str[i])-32)
              if i < len(str)-1 else (chr(ord(str[i])-32))+"\n")
              if ord(str[i]) in range(97, 123) else str[i]), end="")
