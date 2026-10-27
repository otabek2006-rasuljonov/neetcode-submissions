class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        xash = {}
        for i in range(len(nums)):
            if nums[i] not in xash: 
                kerakli = target - nums[i]
                xash[kerakli]=i
            else:
                ans = [xash[nums[i]], i]
        return ans
            