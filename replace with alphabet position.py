def alphabet_position(text):
    out = ""
    text = text.lower()
    for i in text:
        if 96 < ord(i) < 123:
            out += ' ' + str(ord(i)-96)
            print(str(ord(i)-96))
    return out

alphabet_position("The sunset sets at twelve o' clock.")