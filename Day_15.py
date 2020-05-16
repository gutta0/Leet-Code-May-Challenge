class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        maxCurr = A[0]
        maxFinal = A[0]
        minCurr = A[0]
        minFinal = A[0]
        total = A[0]
        for i in range(1, n):
            maxCurr = max(A[i], maxCurr + A[i])
            maxFinal = max(maxCurr, maxFinal)
            
            minCurr = min(A[i], minCurr + A[i])
            minFinal = min(minCurr, minFinal)
            
            total += A[i]
        if total == minFinal:
            return maxFinal
        return max(total - minFinal, maxFinal)
