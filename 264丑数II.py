class Solution:
    def nthUglyNumber(self, n):
        L=[1]*(n+1)
        a=b=c=0
        for i in range(1, n+1):
            A, B, C=L[a]*2, L[b]*3, L[c]*5
            mini=min(A, B, C)
            a+= mini==A
            b+= mini==B
            c+= mini==C
            L[i]=mini
        return L[n-1]