def convert_to_binary(n):

    out = str()

    while n:
        r = n%2
        out = out + str(r)
        n = n//2
    out = out[::-1]
    return out

out = convert_to_binary(12)
print(out)