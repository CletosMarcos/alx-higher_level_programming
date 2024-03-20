#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) in range(97, 123)):
            print("{}".format(chr(ord(str[i])-32)
                  if i < len(str)-1 else (chr(ord(str[i])-32))+"\n"), end="")

        else:
            print("{}".format("\n" if str == "" else str[i]), end="")
