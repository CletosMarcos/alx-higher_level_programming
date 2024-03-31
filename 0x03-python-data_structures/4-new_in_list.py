#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        m_l = my_list.copy()
        m_l[idx] = element
        return m_l
