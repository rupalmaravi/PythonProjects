# nums = [7, 8, 9, 1, 2, 3]
# target = 8
# def two_sum(nums, target):
#    for i in range(len(nums)):
#        for j in range(i + 1, len(nums)):
#            if nums[j] == target - nums[i]:
#                return (i, j)

def two_sums(nums, target):
    hash_map = {}
    # store the element into hash map
    for i in range(len(nums)):
        hash_map[nums[i]] = i
    # for every element , check if target minus number in the list is equal to target , if yes then return indices
    for i in range(len(nums)):
        j = target - nums[i]
        if j in hash_map and hash_map[j] != i:
            return [i, hash_map[j]]


print(two_sums([7, 8, 9, 1, 2, 3], 10))
