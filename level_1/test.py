from re import A


test_list = [1,2,3,4,5]

def print_list(l, nesting):
    
    if not len(l):
        return 

    print(l[0])
    print_list(l[1:], nesting+1)

print_list(test_list,0)

# def print_list(l, nesting):
    
#     lt = len(l)
#     if not lt:
#         return 
#     elif lt == 1:
#         print(l[0])
#     else:
#         print(l[0])
#         print_list(l[1::], nesting+1)

#head first
def print_list_descending(l, nesting):
    
    if not len(l):
        return 

    print(l[-1])
    print_list_descending(l[0:-1], nesting+1)

print_list_descending(test_list,0)

#tail first
def print_list_descending2(l, nesting):
    
    if not len(l):
        return 

    print_list_descending2(l[1:], nesting+1)
    print(l[0])

print_list_descending2(test_list,0)