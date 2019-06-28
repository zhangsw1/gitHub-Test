class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A)-1
        while left<=right:
            mid = (left+right)//2
            if A[mid-1]<A[mid]>A[mid+1]:
                return mid
            elif A[mid-1]<A[mid]<A[mid+1]:
                left = mid+1
            else:
                right = mid-1
if __name__=="__main__":
    sol = Solution()
    print(sol.peakIndexInMountainArray([0,1,2,3,5,0]))
    print(sol.peakIndexInMountainArray([0,2,0]))
    print(sol.peakIndexInMountainArray([0,1,0]))