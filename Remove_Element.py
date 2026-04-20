class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums = [num for num in nums if num != val]
        return nums
    
solution = Solution()
print(solution.removeElement([1,1,2,3,4],1))