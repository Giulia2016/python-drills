class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        out_int = 0
        
        if len(s) < 1 or len(s) > 15:
            raise ValueError("Length of string not valid. <=1 and <= 15")
            
        subtraction_cases = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        
        without_sub_cases = s
        for seq in subtraction_cases.keys():
            out_int += without_sub_cases.count(seq) * subtraction_cases[seq]
            without_sub_cases = without_sub_cases.replace(seq, '')
        
        conv_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        for c in conv_map.keys():
            out_int += without_sub_cases.count(c) * conv_map[c]
            
        return out_int


sol = Solution()

print(sol.romanToInt('LVIII'))
print(sol.romanToInt('MCMXCIV'))
