class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = []
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        while i < len(word1):
            result.append(word1[i])
            i += 1
        while j < len(word2):
            result.append(word2[j])
            j += 1
        return ''.join(result)
    
    
# Test case
sol = Solution()
word1 = "abc"
word2 = "pqr"
print(sol.mergeAlternately(word1, word2))  # Output: "apbqcr"