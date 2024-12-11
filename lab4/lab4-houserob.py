class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1: #neg l baishin baiwl ternii l mungig hulgailh blhor ehnii indexiin utgiig butsaana
            return nums[0]
        
        prev1 = 0 #umnuh baishin hurtl hulgailsn hmgin ih mungu
        prev2 = 0 #umnuhin umnuh baishin hurtl hulgailsn hamgin ih mungu

        for num in nums:
            temp = prev1 #tur huvisagchid prev1 utgiig hadgalj yvna
            prev1 = max(prev1, prev2 + num)
            prev2 = temp

        return prev1
