import sys
from bisect import bisect_left


def find_pos(xs, query):
    # реализация двоичного поиска
    # Invariant 1: low <= pos < high
    # Invariant 2: low <= pos <= high
    low, high = 0, len(xs)
    # Invariant 2: low, high = 0, len(xs)-1
    while low < high:
        # Invariant 2: while low <= high:
        mid = (low + high) // 2
        if query < xs[mid]:
            high = mid  # [low, mid)
            # Inveriant 2: high = mid - 1     # [low, mid-1]
        elif query > xs[mid]:
            low = mid + 1  # [mid+1, high)
        else:
            return mid + 1  # 1-based
    return -1

    # try:
    #     return xs.index(query) + 1
    # except ValueError:
    #     return -1


def find_pos_bisect_left(xs, query):
    low = bisect_left(xs, query)
    # i < low : xs[i] < query
    # i > low : xs[i] > query
    if low < len(xs) and xs[low] == query:
        return low + 1  # 1-based
    else:
        return -1


def test():
    assert find_pos([], 42) == -1
    assert find_pos([42], 42) == 1
    assert find_pos([42], 24) == -1


def test_bisect():
    assert find_pos_bisect_left([], 42) == -1
    assert find_pos_bisect_left([42], 42) == 1
    assert find_pos_bisect_left([42], 24) == -1


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos_bisect_left(xs, query), end=" ")


if __name__ == "__main__":
    test_bisect()
