from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            a = nums2[i]
            for j in range(i, len(nums1)):
                b = nums1[j]
                if b >= a:
                    self.merge(nums1, j, a)
                else:
                    pass

    def merge(self, nums1, start, first):
        temp = []
        for h in nums1:
            temp.append(h)
        for k in range(start, len(nums1)):
            if temp[k] == 0:
                break
            nums1[k+1] = temp[k]
        nums1[j] = first
