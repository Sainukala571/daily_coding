#User function Template for python3
class Solution:
    def evenlyDivides(self, n):
        # code here
        count=0
        s=n
        while n>0:
            r=n%10
            if r!=0:
                if s%r==0:
                    count+=1
            n=n//10
        return count
