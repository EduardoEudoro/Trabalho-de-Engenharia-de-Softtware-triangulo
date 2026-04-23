"""Lucas Crempe Fazan - 828519"""
"""Eduardo Lemos de Oliveira- 824757"""
"""João Victor Dummont Mauad - 834725"""
from dataclasses import dataclass
from enum import Enum, auto
import math


class TriangleType(Enum):
    EQUILATERAL = auto()
    ISOSCELES = auto()
    SCALENE = auto()
    RIGHT = auto()
    INVALID = auto()


@dataclass(frozen=True, slots=True)
class Triangle:
    side1: float
    side2: float
    side3: float

    def _to_float(self, value):
        return float(value)

    def _format(self, x):
        return int(x) if float(x).is_integer() else x

    @property
    def type(self) -> TriangleType:
        try:
            a = self._to_float(self.side1)
            b = self._to_float(self.side2)
            c = self._to_float(self.side3)
        except (TypeError, ValueError):
            return TriangleType.INVALID

        a, b, c = sorted([a, b, c])

        epsilon = 1e-12

        # Valido?
        if a <= 0 or a + b <= c:
            return TriangleType.INVALID

        # Equilátero
        if a == b == c:
            return TriangleType.EQUILATERAL

        # Isósceles
        if a == b or a == c or b == c:
            return TriangleType.ISOSCELES

        # Retângulo (Pitágoras)
        if math.isclose(a**2 + b**2, c**2, rel_tol=epsilon):
            return TriangleType.RIGHT

        # Escaleno
        return TriangleType.SCALENE

    def description(self) -> str:
        try:
            a = float(self.side1)
            b = float(self.side2)
            c = float(self.side3)
        except (TypeError, ValueError):
            return f"Os valores {self.side1}, {self.side2} e {self.side3} são inválidos."

        a, b, c = sorted([a, b, c])

        a_f, b_f, c_f = map(self._format, [a, b, c])

        t = self.type

        if t == TriangleType.INVALID:
            return (
                f"Os números {a_f}, {b_f} e {c_f} NÃO formam um triângulo válido, "
                f"pois a soma de dois lados não é maior que o terceiro ou há lados nulos/negativos."
            )

        if t == TriangleType.EQUILATERAL:
            return (
                f"Os números {a_f}, {b_f} e {c_f} formam um triângulo equilátero, "
                f"pois todos os lados são iguais ({a_f} = {b_f} = {c_f})."
            )

        if t == TriangleType.ISOSCELES:
            if a == b:
                iguais = f"{a_f} = {b_f}"
            elif a == c:
                iguais = f"{a_f} = {c_f}"
            else:
                iguais = f"{b_f} = {c_f}"

            return (
                f"Os números {a_f}, {b_f} e {c_f} formam um triângulo isósceles, "
                f"pois dois lados são iguais ({iguais})."
            )

        if t == TriangleType.RIGHT:
            return (
                f"Os números {a_f}, {b_f} e {c_f} formam um triângulo retângulo, "
                f"pois satisfazem o Teorema de Pitágoras: "
                f"{a_f}² + {b_f}² = {c_f}² ({a**2} + {b**2} = {c**2})."
            )

        return (
            f"Os números {a_f}, {b_f} e {c_f} formam um triângulo escaleno, "
            f"pois todos os lados são diferentes entre si."
        )
