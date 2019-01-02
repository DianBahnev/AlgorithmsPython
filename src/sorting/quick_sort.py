

def quick_sort(numbers, lo, hi):
    if lo < hi:
        p = partition(numbers, lo, hi)
        quick_sort(numbers, lo, p)
        quick_sort(numbers, p+1, hi)


def partition(numbers, lo, hi):
    pivot = numbers[int((lo+hi)/2)]

    while True:

        while numbers[lo] < pivot:
            lo += 1

        while numbers[hi] > pivot:
            hi -= 1

        if lo >= hi:
            return hi

        numbers[lo], numbers[hi] = numbers[hi], numbers[lo]


