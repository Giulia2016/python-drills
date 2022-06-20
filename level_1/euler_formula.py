def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

def euler(n):
    euler = 0
    for i in range(n+1):
        euler += 1/factorial(i)
    return euler


def plot(x):
    out = []
    for i in x:
        line = ' '*(len(x)-i) + '#'*i + '\n'
        print(line)
        out.append(line)
print(euler(7))