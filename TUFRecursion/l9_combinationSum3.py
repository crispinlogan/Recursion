"""
Find all valid combinations of k numbers that sum up to n such that the
following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain
the same combination twice, and the combinations may be returned in any order.
"""

from typing import List


# # WORKS BUT HAS DUPES IN PRINTS
# # ALSO IS PRINTING NOT SAVING TO AN OVERALL LIST
# class Solution:
#     def combinationSum3Helper(self, k: int, n: int, candidates=None, current_list=None) -> List[List[int]]:
#         if current_list is None:
#             current_list = []
#         # base case
#         if len(current_list) == k:
#             if sum(current_list) == n:
#                 print(current_list)
#             else:
#                 return
#         # recursive case
#         for element in candidates:
#             new_current_list = current_list.copy()
#             new_candidates = candidates.copy()
#             new_current_list.append(element)
#             new_candidates.remove(element)
#             self.combinationSum3Helper(k, n, candidates=new_candidates, current_list=new_current_list)
#     #
#     def combinationSum3(self, k: int, n: int):
#         candidates = [1,2,3,4,5,6,7,8,9]
#         return self.combinationSum3Helper(k, n, candidates)


# # WORKS (DUPES IN PRINTS NOW REMOVED) - added `if i >= branch` line and branch as arg
# # ALSO IS STILL PRINTING NOT SAVING TO AN OVERALL LIST
# class Solution:
#     def combinationSum3Helper(self, k: int, n: int, candidates=None, current_list=None, branch=0) -> List[List[int]]:
#         if current_list is None:
#             current_list = []
#         # base case
#         if len(current_list) == k:
#             if sum(current_list) == n:
#                 print(current_list)
#             else:
#                 return
#         # recursive case
#         for i, element in enumerate(candidates):
#             if i >= branch:
#                 new_current_list = current_list.copy()
#                 new_candidates = candidates.copy()
#                 new_current_list.append(element)
#                 new_candidates.remove(element)
#                 self.combinationSum3Helper(k, n, candidates=new_candidates, current_list=new_current_list, branch=i)
#     #
#     def combinationSum3(self, k: int, n: int):
#         candidates = [1,2,3,4,5,6,7,8,9]
#         return self.combinationSum3Helper(k, n, candidates)


# WORKS (DUPES IN PRINTS NOW REMOVED)
# WORKS (NOW RETURNS TO AN OVERALL LIST) - remove self from helper, and put in res and res appends
class Solution:
    def combinationSum3(self, k: int, n: int):
        def combinationSum3Helper(
            k: int, n: int, candidates=None, current_list=None, branch=0
        ):
            if current_list is None:
                current_list = []
            # base case
            if len(current_list) == k:
                if sum(current_list) == n:
                    print(current_list)
                    res.append(current_list)
                else:
                    return
            # recursive case
            for i, element in enumerate(candidates):
                if i >= branch:
                    new_current_list = current_list.copy()
                    new_candidates = candidates.copy()
                    new_current_list.append(element)
                    new_candidates.remove(element)
                    combinationSum3Helper(
                        k,
                        n,
                        candidates=new_candidates,
                        current_list=new_current_list,
                        branch=i,
                    )
            return res

        #
        res = []
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return combinationSum3Helper(k, n, candidates)


s = Solution()
s.combinationSum3(k=2, n=3)  # [[]]


s.combinationSum3(k=3, n=7)  # [[1,2,4]]
s.combinationSum3(k=3, n=9)  # [[1,2,6],[1,3,5],[2,3,4]]


"""
from https://leetcode.com/problems/combination-sum-iii/discuss/60805/Easy-to-understand-Python-solution-(backtracking).
Can use template in similar problems
"""


class Solution(object):
    def combinationSum3(self, k, n):
        ret = []
        self.dfs(list(range(1, 10)), k, n, [], ret)
        return ret

    #
    def dfs(self, nums, k, n, path, ret):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i + 1 :], k - 1, n - nums[i], path + [nums[i]], ret)


s = Solution()
s.combinationSum3(k=2, n=3)  # [[]]


s.combinationSum3(k=3, n=7)  # [[1,2,4]]
s.combinationSum3(k=3, n=9)  # [[1,2,6],[1,3,5],[2,3,4]]


class Solution(object):
    def combinationSum3(self, k, n):
        ret = []
        self.dfs(list(range(1, 10)), k, n, [], ret)
        return ret

    #
    def dfs(self, nums, k, n, path, ret):
        # base case
        if k == 0:
            if n == 0:
                ret.append(path)
            return
        # return early base case
        if n < 0:
            return
        # recursive case
        for i in range(len(nums)):
            self.dfs(nums[i + 1 :], k - 1, n - nums[i], path + [nums[i]], ret)


s = Solution()
s.combinationSum3(k=2, n=3)  # [[]]


s.combinationSum3(k=3, n=7)  # [[1,2,4]]
s.combinationSum3(k=3, n=9)  # [[1,2,6],[1,3,5],[2,3,4]]


# can also look at https://www.youtube.com/watch?v=J2hcPZRpbMk for another recursive solution
