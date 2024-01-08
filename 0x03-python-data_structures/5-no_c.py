#!/usr/bin/python3
def no_c(my_string):

    copy_list = ''

    for i in my_string:
        if i != 'c' and i != 'C':
            copy_list += i

    return (copy_list)
