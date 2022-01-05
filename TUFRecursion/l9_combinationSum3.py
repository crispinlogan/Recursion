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
    def combinationSum3Helper(k: int, n: int, candidates=None, current_list=None, branch=0) -> List[List[int]]:
        if current_list is None:
            current_list = []
        # base case
        if len(current_list) == k:
            if sum(current_list) == n:
                print(current_list)
            else:
                return
        # recursive case
        for i, element in enumerate(candidates):
            if i >= branch:
                new_current_list = current_list.copy()
                new_candidates = candidates.copy()
                new_current_list.append(element)
                new_candidates.remove(element)
                self.combinationSum3Helper(k, n, candidates=new_candidates, current_list=new_current_list, branch=i)
    #
    def combinationSum3(self, k: int, n: int):
        candidates = [1,2,3,4,5,6,7,8,9]
        return self.combinationSum3Helper(k, n, candidates)


s = Solution()
s.combinationSum3(k=2, n=3) # [[]]


s.combinationSum3(k=3, n=7) # [[1,2,4]]
s.combinationSum3(k=3, n=9) # [[1,2,6],[1,3,5],[2,3,4]]
