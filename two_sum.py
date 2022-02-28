# nums = [7, 8, 9, 1, 2, 3]
# target = 8
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return (i, j)


print(two_sum([7, 8, 9, 1, 2, 3], 10))
