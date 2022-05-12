def duplicate_encode(word):
    word = word.lower()
    for i in word:
        if word.count(i) > 1:
            word = word.replace(i, ')')
        else:
            word = word.replace(i, '(')
    return word

print(duplicate_encode("din"))