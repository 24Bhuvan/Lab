def SelectionSort(nums):
    n=len(nums)
    for i in range(n-1):
        minpos=i
        for j in range(i+1,n):
            if nums[j]<nums[minpos]:
                minpos=j
        nums[i],nums[minpos]=nums[minpos],nums[i]
    return nums
nums=[100,99,5,66,8,999,55,44,61]
print(SelectionSort(nums))