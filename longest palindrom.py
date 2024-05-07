class Solution:
    def longestPalindrome(self, s: str) -> str:
       
        lst=[]
        lst1=[]
        if len(s)==1:
            return s
        else:
            for i in range(0,len(s)-1):
                for j in range(i+1,len(s)+1):
                    lst1.append(s[i:j])
            lst=sorted(lst1,key=len)
            lst.reverse()
            for i in lst:
                if i==i[::-1]:
                    return i
                    break
