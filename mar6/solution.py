def max_non_adjacent_sum(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return max(0,nums[0])
    
    incl = 0 # sum with the current element
    excl = 0 # sum without the current element

    for num in nums:
        new_excl = max(incl, excl)
        incl = excl + num
        excl = new_excl

    return max(incl, excl, 0)


