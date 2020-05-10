class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust == [] and N == 1:
            return 1
        truster = set()
        trusted = set()
        count = dict()
        for p in trust:
            truster.add(p[0])
            trusted.add(p[1])
            if p[1] not in count:
                count[p[1]] = 1
            else:
                count[p[1]] += 1
        trusted -= truster
        if len(trusted) > 1 or len(trusted) < 1:
            return -1
        judge = trusted.pop()
        if count[judge] == N - 1:
            return judge
        else:
            return -1
