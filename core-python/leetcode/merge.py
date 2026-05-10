from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1
        j=n-1
        k=m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1

# Test case
sol = Solution()
nums1 = [1,2,3,9,88, 21, 23]
m = 4
nums2 = [2,5,6]
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1)
