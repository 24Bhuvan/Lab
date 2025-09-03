def SelectionSort(nums):
   
    for i in range(len(nums)-1):
        minpos=i
        for j in range(i,len(nums)):
            if nums[minpos]>nums[j]:
                minpos=j
        nums[i],nums[minpos]=nums[minpos],nums[i]