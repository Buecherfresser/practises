def count_bits(n):
    return str.format(bin(n)).count("1")


print(count_bits(7))