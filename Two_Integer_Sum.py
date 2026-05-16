class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum_of = numbers[l] + numbers[r]
            if sum_of < target:
                l += 1
            elif sum_of > target:
                r -= 1
            else:
                return [l+1,r+1]
        return []
        
res = Solution()
print(res.twoSum([-1,0],-1))