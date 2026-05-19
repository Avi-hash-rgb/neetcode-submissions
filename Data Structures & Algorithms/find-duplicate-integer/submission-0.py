class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        num = 0

        for key, freq in counter.items():
            if freq > 1:
                num = key
        return num