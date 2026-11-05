class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = len(nums)
        result = [1] * a

        prefix = 1
        for i in range(a):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(a - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result