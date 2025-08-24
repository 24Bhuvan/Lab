def InsertionSort(nums):
    n=len(nums)
    for i in range(1,n):
        idx=i
        while nums[idx-1]>nums[idx] and idx>0:
            nums[idx],nums[idx-1]=nums[idx-1],nums[idx]
            idx-=1
    return nums
nums=[12,66,9548,445,55,5,54655]
print(InsertionSort(nums))