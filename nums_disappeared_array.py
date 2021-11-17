#Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
nums = [4,3,2,7,8,2,3,1]

def findDisappearedNumbers(nums):
    n = len(nums)
    all_nums = set(range(1, n + 1))

    for i in nums:
        if i in all_nums:
            all_nums.remove(i)

    return list(all_nums)

print(findDisappearedNumbers(nums))