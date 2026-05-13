from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result=[]
        
        for candy in candies:
            if candy + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result
    
# Test case
sol = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(sol.kidsWithCandies(candies, extraCandies))  # Output: [True, True, True, False, True]