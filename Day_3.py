#If not using leet code, would require an import for the Counter method
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        mag = Counter(magazine)
        for c, count in ran:
            if c not in mag:
                return False
            else:
                if count > mag
