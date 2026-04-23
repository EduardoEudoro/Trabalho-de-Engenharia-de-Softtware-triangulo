import pytest
from triangle import Triangle, TriangleType

def test_equilateral():
    t = Triangle(7, 7, 7)
    assert t.type == TriangleType.EQUILATERAL

def test_isosceles():
    assert Triangle(5, 5, 3).type == TriangleType.ISOSCELES
    assert Triangle(5, 3, 5).type == TriangleType.ISOSCELES
    assert Triangle(3, 5, 5).type == TriangleType.ISOSCELES

def test_scalene():
    t = Triangle(3, 4, 5)
    assert t.type == TriangleType.SCALENE

def test_invalid_triangle_inequality():
    assert Triangle(1, 2, 3).type == TriangleType.INVALID
    assert Triangle(1, 2, 4).type == TriangleType.INVALID

@pytest.mark.parametrize("a, b, c", [
    (0, 4, 5), (4, 0, 5), (5, 4, 0),
    (-1, 2, 2), (2, -1, 2), (2, 2, -1),
    (0, 0, 0), (-5, -5, -5)
])
def test_invalid_zeros_and_negatives_permutations(a, b, c):
    assert Triangle(a, b, c).type == TriangleType.INVALID

def test_float_sides():
    assert Triangle(2.5, 2.5, 3.0).type == TriangleType.ISOSCELES
    assert Triangle(3.33, 3.33, 3.33).type == TriangleType.EQUILATERAL
    assert Triangle(1.5, 2.5, 3.5).type == TriangleType.SCALENE


def test_string_numbers_converted_successfully():
    assert Triangle("5", "5", "5").type == TriangleType.EQUILATERAL
    assert Triangle("3", "4", "5").type == TriangleType.SCALENE

def test_invalid_data_types_raise_exception():
    with pytest.raises((TypeError, ValueError)):
        Triangle("a", "b", "c").type
    
    with pytest.raises((TypeError, ValueError)):
        Triangle(None, 4, 5).type
