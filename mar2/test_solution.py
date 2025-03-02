import pytest
from mar2.solution import cons, car, cdr

# Test cases for cons, car, and cdr functions

def test_basic_pairs():
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4
    assert car(cons('a', 'b')) == 'a'
    assert cdr(cons('a', 'b')) == 'b'


def test_edge_cases():
    assert car(cons(None, 10)) is None
    assert cdr(cons(None, 10)) == 10
    assert car(cons(0, -1)) == 0
    assert cdr(cons(0, -1)) == -1


def test_nested_pairs():
    pair = cons(cons(1, 2), cons(3, 4))
    assert car(car(pair)) == 1
    assert cdr(car(pair)) == 2
    assert car(cdr(pair)) == 3
    assert cdr(cdr(pair)) == 4


def test_deeply_nested_pairs():
    pair = cons(cons(cons(1, 2), 3), 4)
    assert car(car(car(pair))) == 1
    assert cdr(car(car(pair))) == 2
    assert cdr(car(pair)) == 3
    assert cdr(pair) == 4


def test_various_data_types():
    assert car(cons([1, 2], (3, 4))) == [1, 2]
    assert cdr(cons([1, 2], (3, 4))) == (3, 4)
    assert car(cons({'key': 'value'}, {1, 2, 3})) == {'key': 'value'}
    assert cdr(cons({'key': 'value'}, {1, 2, 3})) == {1, 2, 3}
