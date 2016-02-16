'''
ref: 
	https://en.wikipedia.org/wiki/Median_of_medians
'''
from math import floor
from math import ceil

def swap(i, j, nums):
    buf = nums[j]
    nums[j] = nums[i]
    nums[i] = buf

# group list to two parts, greater than / less than nums[pivotIndex]
def partition(nums, left, right, pivotIndex):
	pivotValue = nums[pivotIndex]
	swap(pivotIndex, right, nums)
	storeIndex = left
	for i in range(left, right):
		if nums[i] < pivotValue:
			swap(storeIndex, i, nums)
			storeIndex += 1
	# move pivot to it's final place
	swap(right, storeIndex, nums)
	return storeIndex

# implement with insertion sort
def partition5(nums, left, right):
	for i in range(left, right+1):
		j = i
		while j > 0 and nums[j] < nums[j-1]:
			swap(j-1, j, nums)
			j -= 1
	return (left + right) / 2

def pivot(nums, left, right):
	if right - left < 5:
		return partition5(nums, left, right)
	i = left
	while i < right:
		subRight = i + 4
		if subRight > right:
			subRight = right
		median5 = partition5(nums, i, subRight)
		swap(median5, left + floor((i - left)/5), nums)
		i += 5
	return select(nums, left, left + ceil((right - left)/5) - 1, left + (right - left)/10)

def select(nums, left, right, n):
	if left == right:
		return left
	while True:
		pivotIndex = pivot(nums, left, right)
		pivotIndex = partition(nums, left, right, pivotIndex)
		if n == pivotIndex:
			return n
		elif n < pivotIndex:
			right = pivotIndex - 1
		else:
			left = pivotIndex + 1

if __name__ == '__main__':
	nums = [3,3,1,5,5,7,7,7,7]
	print select(nums, 0, len(nums) - 1, (len(nums) - 1)/2)