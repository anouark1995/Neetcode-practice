class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = (''.join(c for c in s if c.isalnum())).lower()
        i = 0
        j = len(s)-1
        while i<j:
            if s[i] != s[j]:
                subi = s[i+1:j+1] 
                subj = s[i:j]
                return (subi == subi[::-1] or subj == subj[::-1])
            i,j = i+1,j-1
        return True
        

sol = Solution()
print(sol.validPalindrome('abbax'))