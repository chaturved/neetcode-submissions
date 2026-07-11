class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = { 1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M" }

        def find_roman(d, ten_power):
            if d == 4 or d == 9:
                return roman_map[ten_power] + roman_map[(d + 1) * ten_power]
            elif 1 <= d <= 3:
                return d * roman_map[ten_power]
            elif 5 <= d <= 8:
                return roman_map[5 * ten_power] + (d - 5) * roman_map[ten_power]

            

        n = num
        ten_power = 1
        str_lst = []
        while n > 0:
            str_lst.append(find_roman(n % 10, ten_power))
            n //= 10
            ten_power *= 10
        
        return "".join(str_lst[::-1])
            