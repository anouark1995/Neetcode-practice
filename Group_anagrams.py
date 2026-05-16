
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                 count[ord(c) - ord("a")] += 1

            dict[tuple(count)].append(s)  
        return list(dict.values())

    
sol = Solution()
print(sol.groupAnagrams(['cat','tac','bat','atc','eat','tea','ate']))