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

    @property
    def type(self) -> TriangleType:
        try:
            a = self._to_float(self.side1)
            b = self._to_float(self.side2)
            c = self._to_float(self.side3)
        except (TypeError, ValueError):
            return TriangleType.INVALID

        sides = sorted([a, b, c])
        a, b, c = sides

        epsilon = 1e-12

        if a <= 0 or a + b <= c:
            return TriangleType.INVALID

        if a == b == c:
            return TriangleType.EQUILATERAL

        if a == b or a == c or b == c:
            return TriangleType.ISOSCELES

        if math.isclose(a**2 + b**2, c**2, rel_tol=epsilon):
            return TriangleType.RIGHT

        return TriangleType.SCALENE

    def description(self) -> str:
        """Gera uma mensagem amigável sobre o triângulo."""
        try:
            a = float(self.side1)
            b = float(self.side2)
            c = float(self.side3)
        except (TypeError, ValueError):
            return f"Os valores {self.side1}, {self.side2} e {self.side3} são inválidos."

        t = self.type

        if t == TriangleType.INVALID:
            return f"Os números {a}, {b} e {c} NÃO formam um triângulo válido."

        if t == TriangleType.EQUILATERAL:
            return f"Os números {a}, {b} e {c} formam um triângulo equilátero."

        if t == TriangleType.ISOSCELES:
            return f"Os números {a}, {b} e {c} formam um triângulo isósceles."

        if t == TriangleType.RIGHT:
            return f"Os números {a}, {b} e {c} formam um triângulo retângulo."

        return f"Os números {a}, {b} e {c} formam um triângulo escaleno."
