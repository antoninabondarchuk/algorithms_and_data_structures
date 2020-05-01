def isValid(s):
    brackets = {')': '(', ']': '[', '}': '{'}
    stack = list()
    for b in s:
        if b in brackets:
            top_element = stack.pop() if stack else None
            if top_element != brackets.get(b):
                return False
        else:
            stack.append(b)

    return not stack


if __name__ == '__main__':
    result1 = isValid('()[{}]')
    print(result1)
