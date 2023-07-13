#!/usr/bin/python3
# program that prints all the names defined by the compiled module

if __name__ == "__main__":
    import hidden_4

    for name in sorted(dir(hidden_4)):
        if name[:2] != '__':
            print("{}".format(name))
