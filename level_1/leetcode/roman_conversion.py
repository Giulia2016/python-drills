
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        accepted_symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        numbers = [1, 5, 10, 50, 100, 500, 1000]
        numbers_list = []

        number_converter = dict(zip(accepted_symbols, numbers))       

        for r in s:
            if not r in accepted_symbols:
                raise ValueError('One of the symbols in the input string is not a roman digit')
            number = number_converter.get(r)

            numbers_list.append(number)

        n = 0
        idx = 0

        while idx < len(numbers_list)-1:

            if numbers_list[idx] == 1:
                if (numbers_list[idx+1] == 5)  | (numbers_list[idx + 1] == 10):
                    n = numbers_list[idx+1] - numbers_list[idx]
                    idx +=2
                    continue
            if (numbers_list[idx] == 10) and (numbers_list[idx+1] == 50) | (numbers_list[idx + 1] == 100):
                    n = numbers_list[idx+1] - numbers_list[idx]
                    idx+=2   
                    continue        
            if numbers_list[idx] == 100:
                if numbers_list[idx+1] == 500 | numbers_list[idx + 1] == 1000:
                    n = numbers_list[idx+1] - numbers_list[idx]          
                    idx+=2
                    continue
            else:
                n = n + numbers_list[idx]
                idx+=1


        return n

solution = Solution()           
print(solution.romanToInt('IIX'))