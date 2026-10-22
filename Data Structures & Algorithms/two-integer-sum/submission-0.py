class Solution:  #0,3 1,4 2,5 3,6
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a ={}
        for i,j in enumerate(nums):
            b = target-j
            if b in a:
                return [a[b],i]
            a[j] = i
                  

        