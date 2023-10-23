def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for a in range(x):
        try:
            if type(my_list[a]) is int:
                print("{:d}".format(my_list[a]), end = " ")
                counter += 1
        except (ValueError, TypeError):
            break
    print()
    return(counter)
