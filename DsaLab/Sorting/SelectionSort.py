def SelectionSort(nums):
    n=len(nums)
    for i in range(n-1):
        minpos=i
        for j in range(i+1,n):
            if nums[j]<nums[minpos]:
                minpos=j
        nums[i],nums[minpos]=nums[minpos],nums[i]
    return nums
