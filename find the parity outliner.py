def find_outlier(integers):
    help = 0
    for i in range(3):
        if integers[i] % 2 == 0:
            help += 1
    for i in integers:
        if help > 1:
            if i % 2 != 0:
                return i
        else:
            if i % 2 == 0:
                return i
