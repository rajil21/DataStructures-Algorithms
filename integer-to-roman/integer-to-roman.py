class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 500, 100, 50, 10, 5, 1]
        rom = ["M", "D", "C", "L", "X", "V", "I"]
        cur = 0
        val = ""
        for i in range(len(values)):
            if cur == i and cur != len(values) - 1:
                cur += 2
            if num/values[i] >= 1:
                val += (rom[i] * (num//values[i]))
                num = num % values[i]
            if values[i] - num <= values[cur] and i != len(values) - 1:
                val += rom[cur]
                val += rom[i]
                num = num % values[cur]               
        return val