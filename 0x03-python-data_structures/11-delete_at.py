#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del(my_list[idx])
    return(my_list)

vi 12-switch.py

#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
