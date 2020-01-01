class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 == str2 * int(len(str1) / len(str2)):
            return str2

        for i in range(1, len(str2)):
            if (str1 == str2[:-i] * int(len(str1) / (len(str2) - i))) and (
                    str2 == str2[:-i] * int(len(str2) / (len(str2) - i))):
                return str2[:-i]

        return ''