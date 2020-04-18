class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1+l2) % 2 == 1:
            return self.find_kth(nums1, nums2, (l1+l2)/2+1)
        else:
            return (self.find_kth(nums1, nums2, (l1+l2)/2) + self.find_kth(nums1, nums2, (l1+l2)/2+1))/2.0

    def find_kth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.find_kth(nums2, nums1, k)

        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        p1 = min(k/2, len(nums1))
        p2 = k-p1
        if nums1[p1-1] < nums2[p2-1]:
            return self.find_kth(nums1[p1:], nums2, k-p1)
        elif nums1[p1-1] > nums2[p2-1]:
            return self.find_kth(nums1, nums2[p2:], k-p2)
        else:
            return nums1[p1-1]
