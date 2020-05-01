def more_frequent_item(lst, item1, item2):
    if lst.count(item1) > lst.count(item2):
        return item1
    elif lst.count(item1) < lst.count(item2):
        return item2
    else:
        return item1


print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))