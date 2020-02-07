class Solution:
    def checkRecord(self, s: str) -> bool:
        A_count = 0
        # L_count = 0
        for i in range(len(s)):
            s1 = s[i:i+3]
            if s[i]=='A':
                A_count += 1
            if A_count > 1:
                return False
            if i<len(s)-2 and s1=='LLL':
                return False
        return True