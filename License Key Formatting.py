class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '')
        length = len(S)
        S = S.upper()
        mod = length % K
        result = ''
        for i in range(mod):
            result += S[i]
        if mod != 0 and mod != length:
            result += '-'
        index = mod
        count = 0
        while index < length:
            result += S[index]
            count += 1
            if count % K == 0 and index != length - 1:
                result += '-'
            index += 1

        return result