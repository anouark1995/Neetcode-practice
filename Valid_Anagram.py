class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))
    
solution = Solution()
print(solution.isAnagram('cat','bat'))
print(solution.isAnagram('cat','tac'))