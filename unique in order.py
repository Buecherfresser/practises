def unique_in_order(iterable):
    h = ""
    counter = 0
    out = []
    for i in iterable:
        if i == h:
            counter += 1
        else:
            out.append(h)
            h = i
    return out.pop()