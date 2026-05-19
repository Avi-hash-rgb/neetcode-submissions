class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        duplicates = False

        for freq, value in counter.items():
            if(value > 1):
                duplicates = True
        return duplicates