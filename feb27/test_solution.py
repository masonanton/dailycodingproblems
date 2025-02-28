import pytest
from feb27.solution import product_except_self

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),  # Basic case
        ([3, 2, 1], [2, 3, 6]),  # Small array
        ([1], [1]),  # Single element
        ([0, 1, 2, 3, 4], [24, 0, 0, 0, 0]),  # Case with one zero
        ([0, 0, 1, 2, 3], [0, 0, 0, 0, 0]),  # Case with multiple zeros
        ([1, -1, 2, -2, 3], [12, -12, 6, -6, 4]),  # Negative numbers
        ([2, 2, 2, 2], [8, 8, 8, 8]),  # All elements the same
        ([10, 20, 30, 40, 50], [1200000, 600000, 400000, 300000, 240000]),  # Large numbers
    ]
)

def test_product_except_self(nums, expected):
    assert product_except_self(nums) == expected

if __name__ == "__main__":
    pytest.main()
