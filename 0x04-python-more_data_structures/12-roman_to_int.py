#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    else:
        roman_letters = [["I", 1], ["V", 5], ["X", 10],
                         ["L", 50], ["C", 100], ["D", 500], ["M", 1000]]

        roman_sum = 0
        last_num = 0

        for letter in roman_string:
            for elem in roman_letters:
                if letter == elem[0]:
                    if last_num == 0 or last_num >= elem[1]:
                        roman_sum += elem[1]
                    else:  # elif last_num < elem[1]
                        roman_sum += elem[1] - (last_num * 2)
                    last_num = elem[1]

    return roman_sum
