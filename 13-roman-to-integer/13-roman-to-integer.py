class Solution:
    def romanToInt(self, s):
        romandic = {'I': 1, 'V': 5, 'X': 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}   
        result = 0
        for i in range(len(s)):
            if i + 1 == len(s) or romandic[s[i]] >= romandic[s[i + 1]] :
                result = result + romandic[s[i]]
            else:
                result = result - romandic[s[i]]
        return result
Task = Solution()
print(Task.romanToInt("III"))
print(Task.romanToInt("LVIII"))
print(Task.romanToInt("MCMXCIV"))
