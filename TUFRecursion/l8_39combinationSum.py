"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen
numbers is different.

It is guaranteed that the number of unique combinations that sum up to target
is less than 150 combinations for the given input.
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(candidates: List[int], target: int, current_list=None, index=0, running_sum=0):
            # print(current_list)
            # sleep(0.5)
            if current_list is None:
                current_list = []
            # base case
            # if sum(current_list) >= target:
            #     if sum(current_list) == target:
            if running_sum >= target:
                if running_sum == target:
                    # print(current_list)
                    res.append(current_list)
                return
            # recursive case
            for i in range(index, len(candidates)):
                # print(i)
                new_list = current_list.copy()
                new_list.append(candidates[i])
                helper(candidates, target, new_list, index=i, running_sum=running_sum+candidates[i])
            return
        res = []
        helper(candidates, target)
        return res


s = Solution()
s.combinationSum([3, 1], 2)
s.combinationSum([3, 1], 3)
s.combinationSum([3, 1, 2], 3)
s.combinationSum([2, 3, 6, 7], 7)







# do .append and .pop instead of copy...
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(candidates: List[int], target: int, current_list=None, index=0, running_sum=0):
            # print(current_list)
            # sleep(0.5)
            if current_list is None:
                current_list = []
            # base case
            # if sum(current_list) >= target:
            #     if sum(current_list) == target:
            if running_sum >= target:
                if running_sum == target:
                    # print(current_list)
                    res.append(current_list.copy())
                return
            # recursive case
            for i in range(index, len(candidates)):
                # print(i)
                # new_list = current_list.copy()
                # new_list.append(candidates[i])
                current_list.append(candidates[i])
                helper(candidates, target, current_list, index=i, running_sum=running_sum+candidates[i])
                current_list.pop()
            return
        res = []
        helper(candidates, target)
        return res
















class Solution:
    def combinationSum(self, candidates: List[int], target: int, current_list=None) -> List[List[int]]:
        # print(f'c = {current_list}')
        if current_list is None:
            current_list = []
        # base case
        if sum(current_list) >= target:
            if sum(current_list) == target:
                print(current_list)
            return
        # recursive case
        # do another recursive call with the first, second, third etc element
        for i in range(len(candidates)):
            current_list.append(candidates[i])
            self.combinationSum(candidates, target, current_list)
            current_list.pop()
        return # return list_of_lists when we do that bit!


s = Solution()
s.combinationSum([3, 1], 2)
s.combinationSum([3, 1], 3)
s.combinationSum([3, 1, 2], 3)
s.combinationSum([2, 3, 6, 7], 7)

"""
Then:
- add to list_of_lists instead of print
- get rid of dupes being printed
    - not nice: could store them as counters then convert to list at end
    - not nice: or just check if new list is already in list_of_lists by using counters each time...
    - better but still not nice: at end just check if new list (as counter) is already in list_of_lists_as_counters by using counters
- optimise for running_sum
- DONE - I NOW .APPEND AND .POP - don't list.copy() each 
"""
