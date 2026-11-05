class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = len(nums)
        result = [0] * a

        for i in range(a):
            prod = 1
            for j in range(a):
                if i == j:
                    continue
                prod *= nums[j]

            result[i] = prod
        return result