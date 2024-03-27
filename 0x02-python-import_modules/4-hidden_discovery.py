#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    dr = dir(hidden_4)
    for i in range(len(dr)):
        st = dr[i]
        if st[0] != "_":
            print(dr[i])
