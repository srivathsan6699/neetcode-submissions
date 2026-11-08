class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_seq = 0
        for i in numset:
            if (i-1) not in numset:
                current_seq = 1
                while (i+current_seq) in numset:
                    current_seq+=1
                longest_seq = max(current_seq,longest_seq)

        return longest_seq



                        


