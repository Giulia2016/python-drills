test = 'Aacdefghijklmnopqrstuvwxyz'


def is_pangram(s):
    import string
    s_unique = set(s.lower())
    s_pan = [i for i in s_unique if i in string.ascii_lowercase]

    if len(s_pan) < 26:
        return False
    else:
        return True

print(is_pangram(test))

