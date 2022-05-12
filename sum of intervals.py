def sum_of_intervals(intervals):
    sum = 0
    counterI = 0

    for i in intervals:
        helpsum = 0
        counterR = 0
        checker = False
        for r in intervals:
            if counterR < counterI:
                if i[1] >= r[1] and i[0] <= r[1]:
                    helpsum = i[1] - r[1]
                    if r[0] - i[0] > 0:
                        helpsum += r[0] - i[0]
                    checker = True
                elif i[0] <= r[0] and i[1] >= r[0]:
                    helpsum = r[0] - i[0]
                    checker = True

            counterR += 1
        if checker == False:
            sum += i[1] - i[0]
        else:
            sum += helpsum
        counterI += 1
    return sum


print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
