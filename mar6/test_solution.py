import pytest
from mar6.solution import max_non_adjacent_sum

def test_basic_cases():
    assert max_non_adjacent_sum([2, 4, 6, 2, 5]) == 13
    assert max_non_adjacent_sum([5, 1, 1, 5]) == 10
    assert max_non_adjacent_sum([3, 2, 7, 10]) == 13
    assert max_non_adjacent_sum([3, 2, 5, 10, 7]) == 15

def test_edge_cases():
    assert max_non_adjacent_sum([]) == 0  # Empty list
    assert max_non_adjacent_sum([5]) == 5  # Single element
    assert max_non_adjacent_sum([-5]) == 0  # Single negative element
    assert max_non_adjacent_sum([0, 0, 0, 0]) == 0  # All zeros
    assert max_non_adjacent_sum([-1, -2, -3, -4]) == 0  # All negative numbers

def test_large_input():
    assert max_non_adjacent_sum([1] * 1000) == 500  # Alternating pick
    assert max_non_adjacent_sum(list(range(1000))) == sum(range(0, 1000, 2))  # Large range input

def test_mixed_values():
    assert max_non_adjacent_sum([4, -1, 3, 8, -5, 6]) == 14  # Mixed positive and negative
    assert max_non_adjacent_sum([-2, 1, 3, -4, 5, -6, 7, 8]) == 18  # Mixed values

if __name__ == "__main__":
    pytest.main()