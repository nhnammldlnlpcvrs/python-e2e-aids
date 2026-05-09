class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Sắp xếp danh sách để tìm chuỗi ngắn nhất
        strs.sort(key=len)
        shortest = strs[0]
        
        for i in range(len(shortest)):
            char = shortest[i]
            for s in strs:
                if s[i] != char:
                    return shortest[:i]  # Trả về phần chung đến vị trí i
        return shortest  # Nếu tất cả chuỗi đều giống nhau, trả về chuỗi ngắn nhất
    
# Test cases
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # ""
print(sol.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # "inters"
print(sol.longestCommonPrefix([""]))  # ""
print(sol.longestCommonPrefix(["a"]))  # "a"
print(sol.longestCommonPrefix(["ab", "a"]))  # "a"