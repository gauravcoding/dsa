import math
class Solution(object):
    def divide(self, dividend, divisor):
        return math.trunc(dividend/divisor)
S1=Solution()
dividend=int(input("Enter dividend number: "))
divisor=int(input("Enter divisor number: "))
print(S1.divide(dividend,divisor))