def resolve_hanoi(n, source, buffer, target):
    """
    :param n: quantity of plats in source
    :param source: initial tower, where we move FROM
    :param buffer: tower to use BETWEEN initial and target
    :param target: where we move TO
    """
    if n > 0:
        resolve_hanoi(n - 1, source, target, buffer)
        if source:
            target.append(source.pop())
        resolve_hanoi(n - 1, buffer, source, target)


if __name__ == '__main__':
    source = [4, 3, 2, 1]
    buffer = []
    target = []
    resolve_hanoi(len(source), source, buffer, target)
    print(source, buffer, target)
