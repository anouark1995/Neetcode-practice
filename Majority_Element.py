class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap={}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:    
                hashmap[n]+=1
        # Now that we have our hashmap
        # We can simply return max(hashmap, key=hashmap.get) which will return the number with the highest numbers of iteration
        # But because the exercise states to return the number with 50% or more cases we add the following     
        if max(hashmap.values()) > (len(nums)/2):
            return max(hashmap, key =hashmap.get)

            

                

solution = Solution()
print(solution.majorityElement([1,3,5,10,5,5,10,10,10,10,10]))