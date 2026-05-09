class Solution:
    '''
        def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Dùng hash map để lưu số đã gặp và index của nó"""
        seen = {}  # number -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]  # Trả về index của complement và index hiện tại
            seen[num] = i  # Lưu số hiện tại vào seen
        return []'''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]==target:
                return [i,j]
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1
        return []
            


# Test cases
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(sol.twoSum([3, 2, 4], 6))        # [1, 2]
print(sol.twoSum([3, 3], 6))           # [0, 1]