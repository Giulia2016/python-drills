ll = [1, 2, [1.2, 'a',3], [4,[5]], [6],16 ,[[12]],7, 9.14, [['pippo']]]
test2 = [[1.45, 0.999, 3], [3,45, 0, 6, 7], [7, 5,'absbs', 4],7]
empty = []

b = 4
def a():
    print(b)
a()


def flatten_list(ll, out_list = []):

    for l in ll:
        if  isinstance(l, list):
            flatten_list(l, out_list)

        else:
            out_list.append(l)

    return out_list

out = flatten_list(ll)
#out = flatten_list(test2, out_list=[])


print(out)

def flatten_list(ll, nesting):
    print(f'{nesting=}')
    out_list = []
    for l in ll:
        if  isinstance(l, list):
            
            out_list += flatten_list(l, nesting +1)

        else:
            #out_list.append(l)
            out_list += [l]

    return out_list
print(ll)
out = flatten_list(ll,0)
print(out)