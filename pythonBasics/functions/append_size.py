def append_size(lst):
    lst += [len(lst)]
    return lst


print(append_size([23, 42, 108]))
