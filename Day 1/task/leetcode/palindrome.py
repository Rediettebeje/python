# to check if the string is palindrome we can use two pointers
# one starting at the beginning,and one starting at the end
# at each iteration we compare the characters left and right
# if they are not equal we return false, otherwise we move them inwards until they meet


# this fun returns True as soon as it finds a single matching pair of
# characters (s[right] == s[left]), which is incorrect. Instead, it should check all
# character pairs before determining if the string is a palindrome.
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[right] == s[left]:
            return True
        left += 1
        right -= 1
    return False

# corrected fun

def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True



st = "abcdtcba"

check = is_palindrome(st)
check1 = isPalindrome(st)
print(check)
print(check1)