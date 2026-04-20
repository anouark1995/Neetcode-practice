class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longestPrefix = []
        for i, letter in enumerate(zip(*strs)):
            if len(set(letter)) == 1:
                longestPrefix.append(letter[0])
            else:
                longestPrefix_str = ""
                break
        longestPrefix_str = "".join(longestPrefix)
        return longestPrefix_str
    
solution = Solution()
print(solution.longestCommonPrefix(['knternational', 'intercontinental', 'interconfederation']))