class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        return len(set(nums))
    #The above method works, but fot the sake of the problem using  Two Pointers
    def removeDuplicates_2(self, nums: list[int]) -> int:
        l = len(nums)
        i=j=0
        while i < l:
            nums[j] = nums[i]
            while i<l and nums[i] == nums[j]:
                i+=1
            j+=1
        return j    


sol = Solution()
print(sol.removeDuplicates_2([1,1,2,6,7]))