class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            i = 0
            j = 0
            comb_word = []
            while i< len(word1) and j< len(word2):
                  comb_word.append(word1[i])
                  comb_word.append(word2[j])
                  i+=1
                  j+=1
            while i< len(word1):
                  comb_word.append(word1[i])
                  i+=1
            while j< len(word2):
                  comb_word.append(word2[j])
                  j+=1
            comb_word = ''.join(comb_word) 
            return comb_word 
                  

sol = Solution()
print(sol.mergeAlternately('abc','xyztttt'))