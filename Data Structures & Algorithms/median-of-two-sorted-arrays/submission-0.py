class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        i, j = 0, 0
        m1, m2 = 0, 0
        
        for index in range(total // 2 + 1):
            m2 = m1

            if i < len(nums1) and j < len(nums2):
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1

            else:
                if i < len(nums1):
                    m1 = nums1[i]
                    i += 1
                else:
                    m1 = nums2[j]
                    j += 1
        
        return (m1 + m2) / 2.0 if total % 2 == 0 else float(m1)


