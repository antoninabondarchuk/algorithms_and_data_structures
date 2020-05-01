def generate(self, numRows: int) -> List[List[int]]:
    stack_result = [[1], ]
    rows_last = numRows - 1
    prev_len = 1
    while rows_last:
        level_stack = [1, 1]
        for i in range(1, prev_len - 1):
            level_stack.insert(i, stack_result[-1][i - 1] + stack_result[-1][i])
        stack_result.append(level_stack)
        prev_len += 1
        rows_last -= 1
    return stack_result