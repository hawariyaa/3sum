# the question is find 3 numbers that add to 0
# example: Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# so the first mehtod we can use is bruteforce checking all elements if they add up to 0
# but this way will have a time complexity of O(n ** 3) and that is not efficent
# we sorted it becuse to avoid duplication, trying the same number again
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums)  - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        yess = [nums[i], nums[j], nums[k]]
                        if yess not in res:
                           res.append(yess)
        return res
nums = [-1,0,1,2,-1,-4]
answer = Solution()
solution = answer.threeSum(nums)
print(solution)

# know lets use a different approach where we can reduce the time complexity to O(n ** 2) and
# space complexity to O(n)
# n Python, enumerate is a built-in function that helps you iterate through a sequence
# (such as a list, tuple, or string) while also keeping track of the index of the current item.
# i and a, i is the index and a is the value so enumerate helps us to keep track of both the index
# and the value at the same time.
class solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
nums = [-1,0,1,2,-1,-4]
answer = solution()
sol = answer.threeSum(nums)
print(sol)






















