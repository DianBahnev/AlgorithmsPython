from copy import copy


def merge(l1, l2):
    merged = []

    while True:
        if l1[0] <= l2[0]:
            merged.append(l1.pop(0))
        else:
            merged.append(l2.pop(0))

        if not l1 or not l2:
            break

    if l1:
        merged.extend(l1)
    else:
        merged.extend(l2)

    return merged


def merge_sort(ls):
    if len(ls) > 1:
        left = merge_sort(ls[0: int(len(ls)/2)])
        right = merge_sort(ls[int(len(ls)/2):])
        return merge(left, right)
    return ls


def rotate_right(ls, start, end, steps):
    end = end + 1
    real_steps = steps % (end-start)
    ls[start:end] = ls[end-real_steps:end] + ls[start:end-real_steps]


def merge_in_place(ls, start1, start2, end2):
    while True:
        if start1 == start2 or \
           start2 >= end2:
            return

        if ls[start1] <= ls[start2]:
            start1 += 1
            continue

        if ls[start1] > ls[start2]:
            rotate_right(ls, start1, start2, 1)
            start1 += 1
            start2 += 1


def merge_sort_in_place(ls, start, end):
    if len(ls[start:end]) > 1:
        merge_sort_in_place(ls, start, int((end+start)/2))
        merge_sort_in_place(ls, int((end+start)/2), end)

        merge_in_place(ls, start, int((end+start)/2), end)


