#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in zip(my_list_1, my_list_2):
        result = 0
        try:
            result = i[0] / i[1]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)

    return new_list