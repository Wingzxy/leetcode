class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2 or len(s)==2 and s[0]==s[1]:return s
        if len(s)==2 and s[0]!=s[1]:return s[0]
        count={}
        for i in range(len(s)-1):
            cur1,cur2=s[i],''
            self.CenterExpand(i-1,i+1,cur1,count,s)
            self.CenterExpand(i,i+1,cur2,count,s)
        result = max(count, key=lambda x: count.get(x))
        return result

    def CenterExpand(self,left,right,cur,count,s):
        while left>=0 and right<len(s):
            if s[left]==s[right]:
                cur = s[left] + cur + s[right]
                left-=1;right+=1
            else:break
        left+=1;right-=1
        count[cur]=right-left+1