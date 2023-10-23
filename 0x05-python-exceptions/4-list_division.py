#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for a in range(list_length):
        try:
            answer = my_list_1[a]/my_list_2[a]
        except ZeroDivisionError:
            print("division by 0")
            answer = 0
        except IndexError:
            print("out of range")
            answer = 0
        except TypeError:
            print("wrong type")
            answer = 0
        finally:
            new_list.append(answer)
    return (new_list)
