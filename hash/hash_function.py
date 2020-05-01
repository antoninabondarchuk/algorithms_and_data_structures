from random import shuffle

example_table = list(range(256))
shuffle(example_table)


def hash8(message, table):
    hash = len(message) % 256
    for i in message:
        hash = table[(hash+ord(i)) % 256]
    return hash


if __name__ == '__main__':
    result1 = hash8('tonya', example_table)
    print(result1)
