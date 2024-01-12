class Solution:
    def halvesAreAlike(self, s: str) -> bool:

       N=len(s)
       a = s[:N//2]  
       b = s[N//2:]
       ma=0
       mb=0
       for c in a:
          if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
              ma += 1
          if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
              ma+=1
       for c in b:
          if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
              mb += 1
          if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
              mb+=1
       if ma==mb: return True
       else: return False       
