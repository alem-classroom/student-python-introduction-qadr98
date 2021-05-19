def insert_squares(arr, num):
    i = 0
    list1 = []
    while i < num:
        i += 1
        list1.append(i**2)
    return arr + list1
