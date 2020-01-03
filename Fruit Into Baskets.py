import collections
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) < 3:
            return len(tree)
        basket = collections.defaultdict(int)
        win_start = curr_max = 0
        for win_end in range(len(tree)):
            basket[tree[win_end]] += 1
            while len(basket) > 2:
                basket[tree[win_start]] -= 1
                if basket[tree[win_start]] == 0:
                    del basket[tree[win_start]]
                win_start += 1
            if win_end - win_start + 1 > curr_max:
                curr_max = win_end - win_start + 1
        return curr_max