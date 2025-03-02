def first_missing_positive(nums):
    length = len(nums)

    if length == 0:
        return 1

    # Step 1: clean the array
    for i in range(length):
        if nums[i] <= 0 or nums[i] > length:
            nums[i] = length + 1

    # Step 2: mark the presence of numbers
    for i in range(length):
        num = abs(nums[i])
        if num <= length:
            nums[num - 1] = -abs(nums[num-1])

    # Step 3: find the first missing positive
    for i in range(length):
        if nums[i] > 0:
            return i + 1
        
    return length + 1
    

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp