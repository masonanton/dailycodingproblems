def has_pair_with_sum(nums, k):
    seen = set() # create a set to store the numbers we have seen so far

    for element in nums:
        if k - element in seen:
            return True
        seen.add(element)

    return 0