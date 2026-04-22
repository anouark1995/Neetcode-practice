class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()
        print(s)

        """
        Do not return anything, modify s in-place instead.
        """
    
    # With Two-Pointers:
        i,j = 0,len(s)-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
solution = Solution()
solution.reverseString(["b","a","c","k"])