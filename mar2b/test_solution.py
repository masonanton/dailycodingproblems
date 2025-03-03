import pytest
from mar2b.solution import merge_k_sorted_lists

# Sample test cases for the merge_k_sorted_lists function

def test_empty_lists():
    assert merge_k_sorted_lists([]) == []
    assert merge_k_sorted_lists([[]]) == []
    assert merge_k_sorted_lists([[], [], []]) == []

def test_single_list():
    assert merge_k_sorted_lists([[1, 2, 3]]) == [1, 2, 3]
    assert merge_k_sorted_lists([[5]]) == [5]

def test_two_sorted_lists():
    assert merge_k_sorted_lists([[1, 3, 5], [2, 4, 6]]) == [1, 2, 3, 4, 5, 6]
    assert merge_k_sorted_lists([[1, 4, 7], [2, 5, 8]]) == [1, 2, 4, 5, 7, 8]

def test_multiple_sorted_lists():
    assert merge_k_sorted_lists([[1, 4, 7], [2, 5, 8], [3, 6, 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_k_sorted_lists([[1, 2], [3, 4], [0, 5]]) == [0, 1, 2, 3, 4, 5]

def test_lists_with_duplicates():
    assert merge_k_sorted_lists([[1, 1, 2], [2, 3, 3], [1, 2, 4]]) == [1, 1, 1, 2, 2, 2, 3, 3, 4]
    assert merge_k_sorted_lists([[1, 2, 2], [2, 2, 3], [3, 4, 4]]) == [1, 2, 2, 2, 2, 3, 3, 4, 4]

def test_negative_numbers():
    assert merge_k_sorted_lists([[-3, -1, 2], [-2, 0, 1]]) == [-3, -2, -1, 0, 1, 2]
    assert merge_k_sorted_lists([[-5, -3, -1], [-4, -2, 0]]) == [-5, -4, -3, -2, -1, 0]

def test_mixed_size_lists():
    assert merge_k_sorted_lists([[1, 3], [2], [0, 4, 5]]) == [0, 1, 2, 3, 4, 5]
    assert merge_k_sorted_lists([[1], [2, 3, 4], [0]]) == [0, 1, 2, 3, 4]

def test_large_input():
    large_list = [[i for i in range(1000)]] * 10
    expected = sorted([i for i in range(1000)] * 10)
    assert merge_k_sorted_lists(large_list) == expected