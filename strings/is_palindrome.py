def isPalindrome(s: str) -> bool:
    left_i = 0
    right_i = len(s) - 1
    while left_i < right_i:
        if not s[left_i].isalnum():
            left_i += 1
            continue
        if not s[right_i].isalnum():
            right_i -= 1
            continue
        left = s[left_i].lower() if s[left_i].isalpha() else s[left_i]
        right = s[right_i].lower() if s[right_i].isalpha() else s[right_i]
        if left == right:
            left_i += 1
            right_i -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    result1 = isPalindrome('A man, a plan, a canal: Panama')
    print(result1)
