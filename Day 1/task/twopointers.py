
# since the array is sorted , we can use two pointers,
# we start with the first and last number 1 + 15 = 16 > 13
# since sum is > target we move the right pointer to left to decrease the sum 1 + 14 = 15 > 13
# 1+ 9 = 10 < 13 so now we have to move the left pointer right  to increase the sum
# 2 + 9 = 11 < 13, 4 + 9 = 13 = 13 so the numbers are 4 and 9 we know that since the array is sorted
# there are not other numbers in the array that add up to the target because if we move the left pointer forward
# the sum will become greater than the target, similarly if we move the right pointer backward , the sum will decrease



def check_for_target(nums,target):
    # pointer technique
    left = nums[0]
    right = len(nums)-1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            print(nums[left],nums[right]) #  to print the numbers
            print(left, right) # i to print indices
            print(left + 1, right + 1)  # Convert to 1-based index
            return True

        elif current > target:
            right -= 1
        else:
            left += 1

    return False



nu = [1, 2, 4, 6, 8, 9, 14, 15]
targ = 13

check = check_for_target(nu,targ)
print(check)

