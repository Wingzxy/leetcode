class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        intersert = False
        result = (C-A)*(D-B)+(G-E)*(H-F)
        dx = min(C, G) - max(A, E)
        dy = min(D, H) - max(B, F)
        if(dx > 0 and dy > 0): intersert = True
        area = dx*dy if intersert else 0
        return result - area