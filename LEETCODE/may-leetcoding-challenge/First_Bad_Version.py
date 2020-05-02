# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=1
        e=n
        ans=-1
        while s<=e:
            mid=(s+e)//2
            if isBadVersion(mid):
                e=mid-1
                ans=mid
            else:
                s=mid+1
        return ans