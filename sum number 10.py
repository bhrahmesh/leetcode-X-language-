class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        k={}
        def dfs(i,j):
            if (i,j) in k:
                return k[(i,j)]
            if i >=len(s) and j >=len(s):
                return True 
            if j>=len(p):
                return False
            match = i< len(s) and (s[i] == p[j] or p[j] ==".")
            if (j+1) < len(p) and p[j+1] =="*":
                k[(i,j)] = (dfs(i,j+2)) or (match and dfs(i+1,j))
                return k[(i,j)]
            if match:
                k[(i,j)]= (dfs(i+1,j+1))
                return k[(i,j)]
            k[(i,j)] = False
            return False
        return dfs(0,0)
