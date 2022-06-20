#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

#Note: The function accepts an integer and returns an integer

def square_digits(num):
    squared = []
   
    for d in str(num):
        new_n = int(d)**2
        squared.append(str(new_n))
    return int(''.join(squared))
    
print(square_digits(1099))