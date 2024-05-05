import timeit
from sort_merge import merge_sort
from sort_insertion import insertion_sort


def measure_time(func, data):
    start_time = timeit.default_timer()
    func(data.copy())
    end_time = timeit.default_timer()
    return end_time - start_time


data = [5, 3, 8, 4, 24, 43, 5, 26, 5, 4, 567, 645, 8, 6, 4, 34, 564, 23564, 1323, 38, 795, 53, 67]

merge_sort_time = measure_time(merge_sort, data)
print("Merge Sort execution time:", merge_sort_time)

insertion_sort_time = measure_time(insertion_sort, data)
print("Insertion Sort execution time:", insertion_sort_time)

timsort_time = measure_time(sorted, data)
print("Timsort execution time:", timsort_time)
