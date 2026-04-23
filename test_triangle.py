"""Lucas Crempe Fazan - 828519"""
"""Eduardo Lemos de Oliveira- 824757"""
"""João Victor Dummont Mauad - 834725"""
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
    t = Triangle(4, 5, 6)
    assert t.type == TriangleType.SCALENE
    
def test_invalid_triangle_inequality():
    assert Triangle(1, 2, 3).type == TriangleType.INVALID
    assert Triangle(1, 2, 4).type == TriangleType.INVALID

def test_invalid_zeros_and_negatives_permutations():
    invalid_cases = [
        (0, 4, 5), (4, 0, 5), (5, 4, 0),
        (-1, 2, 2), (2, -1, 2), (2, 2, -1),
        (0, 0, 0), (-5, -5, -5)
    ]
    for a, b, c in invalid_cases:
        assert Triangle(a, b, c).type == TriangleType.INVALID
    
def test_float_sides():
    assert Triangle(2.5, 2.5, 3.0).type == TriangleType.ISOSCELES
    assert Triangle(3.33, 3.33, 3.33).type == TriangleType.EQUILATERAL
    assert Triangle(1.5, 2.5, 3.5).type == TriangleType.SCALENE

def test_string_numbers_converted_successfully():
    assert Triangle("5", "5", "5").type == TriangleType.EQUILATERAL
    assert Triangle("4", "5", "6").type == TriangleType.SCALENE

def test_precision_and_near_equality():
    assert Triangle(5.0, 5.0, 5.0000000001).type == TriangleType.ISOSCELES
    assert Triangle(0.0001, 0.0001, 0.0001).type == TriangleType.EQUILATERAL 

def test_right_triangle_support():
    assert Triangle(5, 12, 13).type == TriangleType.RIGHT
    assert Triangle(6, 8, 10).type == TriangleType.RIGHT
    assert Triangle(8, 15, 17).type == TriangleType.RIGHT
    assert Triangle(3, 4, 5).type == TriangleType.RIGHT

def test_error_messages_and_explanations():    
    desc_right = Triangle(5, 12, 13).description()
    assert "retângulo" in desc_right
    
    desc_invalid = Triangle(0, 5, 5).description()
    assert "NÃO formam um triângulo válido" in desc_invalid
    
    desc_equilateral = Triangle(2, 2, 2).description()
    assert "equilátero" in desc_equilateral

def test_exceptions_and_error_handling():    
    assert Triangle("a", "b", "c").type == TriangleType.INVALID
    assert Triangle(None, 4, 5).type == TriangleType.INVALID
    assert Triangle([1, 2], {3: 4}, 5).type == TriangleType.INVALID
    assert "são inválidos" in Triangle("a", "b", "c").description()
