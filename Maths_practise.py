import math
class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return 1
        elif n<0:
            return 1/pow(x,-n)
        else:
            return pow(x,n)

x = float(input("Enter a value: "))
n = int(input("Enter power value: "))
Sol = Solution()
print(Sol.myPow(x, n))
