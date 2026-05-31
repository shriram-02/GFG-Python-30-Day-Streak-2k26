class Solution:
    def RecursivePower(self, n, p):
        # code here
        if p == 0:
            return 1
        return n * self.RecursivePower(n, p - 1)