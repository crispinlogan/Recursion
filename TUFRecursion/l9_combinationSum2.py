from typing import List


class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ):  # -> List[List[int]]:
        def dfs_helper(candidates, target, path=None, path_sum=0):
            if path is None:
                path = []
            # base case return early
            if path_sum == target:
                ret.append(path)
                return
            # base case
            if len(candidates) == 0:
                return
            # recursive case
            for i in range(len(candidates)):
                if (
                    candidates[i - 1] != candidates[i]
                ):  # see https://leetcode.com/problems/combination-sum-ii/discuss/16944/Beating-98-Python-solution-using-recursion-with-comments
                    dfs_helper(
                        candidates[i + 1 :],
                        target,
                        path=path + [candidates[i]],
                        path_sum=path_sum + candidates[i],
                    )

        #
        ret = []
        candidates.sort()  # see https://leetcode.com/problems/combination-sum-ii/discuss/16944/Beating-98-Python-solution-using-recursion-with-comments
        dfs_helper(candidates, target)
        return ret


s = Solution()
s.combinationSum2(candidates=[1, 2, 3], target=7)  # [[]]
s.combinationSum2(candidates=[1, 2, 3, 4], target=7)  # [[1,2,4], [3,4]]

s.combinationSum2(candidates=[1, 2, 3], target=6)  # [[1,2,3]]


s.combinationSum2(candidates=[1, 2, 2, 3], target=6)  # [[1,2,3]]
s.combinationSum2(candidates=[1, 2, 2, 2, 3], target=6)  # [[1,2,3]]
s.combinationSum2(candidates=[3, 2, 2, 2, 1], target=6)  # [[1,2,3]]

s.combinationSum2(candidates=[2, 2, 2], target=4)  # [[2,2]]

s.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5)  # [[1,2,2], [5]]

s.combinationSum2(
    candidates=[10, 1, 2, 7, 6, 1, 5], target=8
)  # [[1,1,6], [1,2,5], [1,7], [2,6]]


# note this https://www.youtube.com/watch?v=OXU6c6daCYc
# also has a v easy to understand solutin, but I don't think it'soptimal as it checks each time if the sublist
# is in the final list of lists each time before appending...


s.combinationSum2(
    candidates=[
        14,
        6,
        25,
        9,
        30,
        20,
        33,
        34,
        28,
        30,
        16,
        12,
        31,
        9,
        9,
        12,
        34,
        16,
        25,
        32,
        8,
        7,
        30,
        12,
        33,
        20,
        21,
        29,
        24,
        17,
        27,
        34,
        11,
        17,
        30,
        6,
        32,
        21,
        27,
        17,
        16,
        8,
        24,
        12,
        12,
        28,
        11,
        33,
        10,
        32,
        22,
        13,
        34,
        18,
        12,
    ],
    target=27,
)
