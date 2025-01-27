class Solution(object):
    def searchInsert(self, nums, target):
        for index, value in enumerate(nums):
            if value == target:
                return index
        else:
            return "Not found value in the list!!"


target = int(input("Enter a value you want to search: "))
S1 = Solution()
print(S1.searchInsert([1, 3, 5, 6], target))
