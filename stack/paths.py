def simplify_path(path: str) -> str:
    stack = []
    for p in path.split("/"):
        if p == "..":
            if stack:
                stack.pop()
        elif p and p != ".":
            stack.append(p)
    return "/" + "/".join(stack)


if __name__ == '__main__':
    result1 = simplify_path('../..')
    print(result1)

