class Solution:
    def findComplement(self, num: int) -> int:
        bits = bin(num)[2:]
        return num ^ int('1' * len(bits), 2)
        
