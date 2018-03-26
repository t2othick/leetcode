# coding: utf8


class Solution(object):
    def findKth(self, nums1, nums2, s1, e1, s2, e2, k):
        if s1 > e1:
            return nums2[s2+k-1]
        if s2 > e2:
            return nums1[s1+k-1]
        mid1 = (e1 + s1) / 2
        mid2 = (e2 + s2) / 2
        length = (mid1 - s1 + 1) + (mid2 - s2 + 1)

        if nums1[mid1] < nums2[mid2]:
            if length > k:
                return self.findKth(nums1, nums2, s1, e1, s2, mid2 - 1, k)
            else:
                return self.findKth(nums1, nums2, mid1 + 1, e1, s2, e2, k - mid1 - 1 + s1)
        else:
            if length > k:
                return self.findKth(nums1, nums2, s1, mid1 - 1, s2, e2, k)
            else:
                return self.findKth(nums1, nums2, s1, e1, mid2 + 1, e2, k - mid2 -1 + s2)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1 + l2) % 2 == 1:
            return self.findKth(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1, (l1 + l2) / 2 + 1)
        else:
            a = self.findKth(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1, (l1 + l2) / 2)
            b = self.findKth(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1, (l1 + l2) / 2 + 1)
            return (a + b) * 1.0 / 2


def merge(nums1, nums2):
    i = j = 0
    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    res += nums1[i:]
    res += nums2[j:]

    l1 = len(nums1)
    l2 = len(nums2)
    if (l1 + l2) % 2 == 1:
        return res[(l1 + l2) / 2]
    else:
        a = res[(l1 + l2) / 2 - 1]
        b = res[(l1 + l2) / 2]
        return (a + b) * 1.0 / 2


if __name__ == "__main__":
    import random
    NUMS1 = range(1, 50, random.choice(range(5, 9)))
    NUMS2 = range(1, 50, random.choice(range(5, 9)))
    # NUMS1 = [1, 3]
    # NUMS2 = [2]
    print NUMS1, NUMS2
    # print [1, 1, 6, 7, 11, 13, 16, 19, 21, 25, 26]

    s = Solution()
    print "right", merge(NUMS1, NUMS2)
    print "test", s.findMedianSortedArrays(NUMS1, NUMS2)
