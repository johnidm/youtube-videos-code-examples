def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1  # Get the index corresponding to the number
        nums[index] = -abs(nums[index])  # Mark the number at this index as seen (negative)
    print(nums)
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:  # A positive value means this index (plus 1) is missing
            result.append(i + 1)
    
    return result

print(findDisappearedNumbers([1,1]))