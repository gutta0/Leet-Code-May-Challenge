# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        first = n + 1
        if (isBadVersion(1)):
            return 1
        while end >= start:
            mid = (start + end) // 2
            if isBadVersion(mid):
                first = mid
                end = mid - 1
            else:
                start = mid + 1
        return first
