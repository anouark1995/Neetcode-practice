class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        i=0
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
                else:
                    j+=1
            i+=1
        return False
    
sol = Solution()
print(sol.containsNearbyDuplicate([1,5,6,1],3))
