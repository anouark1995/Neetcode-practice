class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums = [num for num in nums if num != val]
        return len(nums)
    
    def removeElement_(self, nums: list[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k

    
solution = Solution()
print(solution.removeElement([1,2,1,3,4],1))
print(solution.removeElement_([1,2,1,3,4],2))
