#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    div_list = []

    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]

        except (ValueError, TypeError):
            div = 0
            print("wrong type")
            pass
        except ZeroDivisionError:
            div = 0
            print("division by 0")
            pass
        except IndexError:
            div = 0
            print("out of range")
            pass

        finally:
            div_list.append(div)
    return div_list
