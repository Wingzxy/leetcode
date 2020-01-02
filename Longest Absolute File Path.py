class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split('\n')
        stack = []
        maxLen = 0

        for subPath in paths:
            currPath = subPath
            depth = 0
            while currPath.startswith('\t'):
                currPath = currPath[1:]
                depth += 1

            while len(stack) > depth:
                a = stack.pop()

            stack.append(len(currPath))
            if '.' in currPath:
                maxLen = max(sum(stack) + len(stack) - 1, maxLen)

        return maxLen