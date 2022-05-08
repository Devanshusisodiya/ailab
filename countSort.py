def countSort(nums: list[int]) -> list:
    countMap = {}
    maxNum = nums[0]
    sortedArr = [0] * len(nums)
    
    for i in nums:
        # GETTING THE MAXIMUM ELEMENT
        # ALONG WITH GETTING THE COUNT OF EVERY ELEMENT
        if i > maxNum:
            maxNum = i
        if i in countMap:
            countMap[i] += 1
        else:
            countMap[i] = 1

    # CREATING EMPTY ARRAY
    countArr = [0] * (maxNum + 1)

    # MAINTAINING THE COUNT ARRAY
    for i in range(maxNum + 1):
        if i in countMap:
            countArr[i] = countMap[i]

    # GETTING CUMULATIVE SUM FOR COUNT ARRAY
    for i in range(1, maxNum + 1):
        countArr[i] = countArr[i] + countArr[i-1]

    # FINAL STEP OF THE ALGORITHM
    # DECREASING THE COUNT AND
    # PLACING ELEMENT AT DECREASED INDEX
    for i in nums:
        countArr[i] = countArr[i] - 1
        index = countArr[i]
        sortedArr[index] = i

    return sortedArr

print(countSort([1,5,2,4,0]))