#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
            continue
        except ZeroDivisionError:
            print("division by 0")
            continue
        except TypeError:
            result.append(0)
            print("wrong type")
            continue
        except IndexError:
            print("out of range")
            continue
        finally:
            pass
    return (result)
