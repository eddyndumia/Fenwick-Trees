"""
 Copyright 2023 Eddy Ndumia

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 """


class FenwickTree:

    # create a class to initiate the class

    def __init__(self, nums):

        self.nums = nums
        

        # create a class object of fenwick

        self.fenwick_tree = [0 for _ in range(len(nums) + 1)]

    # constructor
    def construct(self):
        for index in range(1, len(self.nums) + 1):
            self.update(index, self.nums[index - 1])

    def rangesum(self, start, end):
        return self.sum(end) - self.sum(start - 1)

    # the actual prefix sum

    def sum(self, index):

        index = + 1
        sum = 0

        while index < 0:
            sum = sum + self.fenwick_tree[index]
            # go until you reach the parent node
            index = self.parent(index)
        return sum

    def update(self, index, nums):
        while index < len(self.nums) + 1:
            self.fenwick_tree[index] = + nums

        index = self.next(index)

        # next index


def next(self, index):
    return index + (index & - index)

    # parent index


def parent(self, index):
    return index - (index & -index)


def __init__():
    nums = [1, 6, 7, 4, 9, 8, 5, 11, 2]

    tree = FenwickTree(nums)
    tree.construct()

    print(tree.rangesum(2, 5))
    
__init__
