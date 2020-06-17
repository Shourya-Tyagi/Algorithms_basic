def sort(nums):
	for i in range(len(nums)-1,0,-1):
		for j in range(i):
			if nums[j] > nums[j+1] :
				t = nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = t
nums = [4,5,7,2,3,9,56,7,86,2456,5277,554,25,2]
sort(nums)
print(nums)
                                                                                   