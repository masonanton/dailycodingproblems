import pytest
from feb26.solution import has_pair_with_sum

@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([10, 15, 3, 7], 17, True),  # Basic case with a valid pair
        ([1, 2, 3, 4, 5], 10, False),  # No valid pair
        ([5, 5, 5, 5], 10, True),  # Multiple same elements forming a pair
        ([0, 0, 0, 0], 0, True),  # Pair of zeros
        ([1, 2, 3, 4], 3, True),  # Smallest pair
        ([], 5, False),  # Empty list
        ([5], 5, False),  # Single element
        ([1, -1, 2, -2, 3], 0, True),  # Negative numbers forming a pair
        ([10, 20, 30, 40], 70, True),  # Large numbers forming a pair
        ([10, 20, 30, 40], 100, False),  # Sum too large to be possible
    ]
)

def test_has_pair_with_sum(nums, k, expected):
    assert has_pair_with_sum(nums, k) == expected

if __name__ == "__main__":
    pytest.main()

    
