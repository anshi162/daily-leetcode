class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        l=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a=s[:n//2]
        b=s[n//2:]
        c,d=0,0
        for i in range(len(a)):
            if a[i] in l:
                c+=1
            if b[i] in l:
                d+=1
        if c==d:
            return True
        return False
