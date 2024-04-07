#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        bs = next(iter(a_dictionary.values()))
        k = next(iter(a_dictionary.keys()))

        for i, j in a_dictionary.items():
            if bs < j:
                bs = j
                k = i

        return k
