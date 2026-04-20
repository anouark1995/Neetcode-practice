class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        HashMap={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in HashMap:
                return [HashMap[diff],i]
            HashMap[n]=i
        return
    
solution=Solution()
print(solution.twoSum([1,3,7,6],9))