from math import factorial as f


def getRow(rowIndex: int):
    result_row = []
    for i in range(rowIndex):
        cnk = int(f(rowIndex) / (f(i) * (f(rowIndex - i))))
        result_row.append(cnk)
    return result_row


if __name__ == '__main__':
    result1 = getRow(9)
    print(result1)
