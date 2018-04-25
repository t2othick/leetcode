func removeElement(nums []int, val int) (j int) {

	length := len(nums)
	for i := 0; i < length; i ++ {
		if nums[i] != val {
			nums[j] = nums[i]
			j ++
		}
	}

	return j
}
