class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = dict()
        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        for key, value in letters.items():
            if value == 1:
                return s.index(key)
        return -1
