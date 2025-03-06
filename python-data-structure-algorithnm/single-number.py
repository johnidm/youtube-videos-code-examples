"""
Single Number - Using Sorting Approach
"""

def single_number(nums: list[int]) -> int:
    nums.sort()

    for i in range(0, len(nums) -1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]

    return nums[-1]


print(single_number([2, 2, 1]))
print(single_number([4, 3, 3, 2, 2]))
