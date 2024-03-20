#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)+1):
        if (ord(str[i]) in range(97, 123)):
            print("{}".format(chr(ord(str[i])-32)
                  if i < len(str)-1 else (chr(ord(str[i])-32))+"\n"), end="")

        else:
            print("{}".format(str[i]), end="")
