def canJump(self, nums: List[int]) -> bool:
	i = 0
	max_reach = 0
	while (i < len(nums)) :
		if (max_reach < i):
			return False
		if (max_reach < nums[i] + i):
			max_reach = nums[i] + i
		i = i + 1
	return True
