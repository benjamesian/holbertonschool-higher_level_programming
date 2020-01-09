#!/usr/bin/python3

def find_peak_helper(start, stop, l):
    if start >= stop:
        return None

    length = len(l)
    mid = start + ((stop - start) // 2)
    if mid > length:
        return None
    vl = l[mid - 1]
    v = l[mid]
    vr = l[(mid + 1) % length]

    if vl == v == vr or vl < v > vr:
        return v

    lpeak = None if mid == stop else find_peak_helper(start, mid, l)
    if lpeak is not None:
        return lpeak
    return None if mid == start else find_peak_helper(mid, stop, l)

def find_peak(list_of_integers):
    length = len(list_of_integers)
    if length == 0:
        return None
    elif length <= 2:
        return max(list_of_integers)
    return find_peak_helper(0, length, list_of_integers)

print(find_peak([1, 2, 3, 4, 5]))
print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 3, 1]))
