"""
    >>> seq = range(10)
    >>> rv1 = search(seq, 0)
    >>> rv2 = search(seq, 9)
    >>> rv3 = search(seq, -1)
    >>> rv1
    0
    >>> rv2
    9
    >>> rv3
"""


def search(seq, key):
    lo = 0
    hi = len(seq) - 1

    while hi >= lo:
        mid = lo + (hi - lo) // 2
        if seq[mid] < key:
            lo = mid + 1
        elif seq[mid] > key:
            hi = mid - 1
        else:
            return mid
    return False
