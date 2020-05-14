class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        if k >= len(num):
            return "0"
        stack = []
        n = len(num)
        for n in num:
            while len(stack) > 0 and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        if k > 0:
            stack = stack[:-k]
        if len(''.join(stack).lstrip('0')) == 0:
            return "0"
        return ''.join(stack).lstrip('0')
            
            
