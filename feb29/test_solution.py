import pytest
from feb29.solution import first_missing_positive

# Test cases for the first missing positive function

def test_basic_cases():
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1


def test_edge_cases():
    assert first_missing_positive([]) == 1  # Empty array
    assert first_missing_positive([1]) == 2  # Single element, correct start
    assert first_missing_positive([2]) == 1  # Single element, missing 1


def test_all_negatives():
    assert first_missing_positive([-3, -2, -1]) == 1  # All negative numbers


def test_all_positives_in_order():
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6


def test_with_duplicates():
    assert first_missing_positive([1, 2, 2, 3, 4]) == 5
    assert first_missing_positive([1, 1, 0, -1, 2]) == 3


def test_with_large_gaps():
    assert first_missing_positive([100, 101, 102]) == 1
    assert first_missing_positive([1, 100, 200]) == 2


def test_unordered_array():
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([2, 1, 3, 5, 4, 6, 8]) == 7