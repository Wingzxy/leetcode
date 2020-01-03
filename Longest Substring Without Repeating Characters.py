class Solution:
    # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxval = 0
        for i in range(len(s)):
            l1 = []
            l1.append(s[i])
            maxval = max(len(l1),maxval)
            for j in range(i+1,len(s)):
                if s[j] not in l1:
                    l1.append(s[j])
                    maxval = max(len(l1),maxval)
                else:
                    break
        return maxval

    # O(n)
    def lengthOfLongestSubstring2(self, s: str) -> int:
        wstr = ''
        lgst = 0
        for w in s:
            if w not in wstr:
                wstr = wstr + w
                if len(wstr) >= lgst:
                    lgst = len(wstr)


            else:
                wstr = wstr[wstr.rindex(w) + 1:] + w

        return lgst