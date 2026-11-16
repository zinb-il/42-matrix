
from numbers import Number
from typing import Generic, TypeVar
from .complex import Complex

K = TypeVar("K", "Complex", float, int)

# ABS function
def _abs(n : K):
    if isinstance(n, (float, int)):
        return n if n > 0.0 else -n
    if isinstance(n, Complex):
        return n._my_abs__()
    #This condition only for test
    if isinstance(n, complex):
        return abs(n)

def _is_number(value: object) -> bool:
    return isinstance(value, (Number, Complex)) and not isinstance(value, bool)


class Vector(Generic[K]):
    """A vector containing numeric elements."""

    def __init__(self, data: list[K]):
        if not data:
            raise ValueError("A vector cannot be empty")

        if not all(_is_number(x) for x in data):
            raise TypeError("Vector elements must be numbers")

        self.data = list(data)
        self.shape = len(self.data)

    def __repr__(self) -> str:
        return "\n".join(f"[{x}]" for x in self.data)

    def add(self, v: "Vector[K]") -> "Vector[K]":
        if not isinstance(v, Vector):
            return NotImplemented
        if self.shape != v.shape:
            raise ValueError("Vectors must have the same size")

        for i in range(self.shape):
            self.data[i] += v.data[i]

        return self

    def sub(self, v: "Vector[K]") -> "Vector[K]":
        if not isinstance(v, Vector):
            return NotImplemented
        if self.shape != v.shape:
            raise ValueError("Vectors must have the same size")

        for i in range(self.shape):
            self.data[i] -= v.data[i]

        return self

    def scl(self, a: K) -> "Vector[K]":
        if not _is_number(a):
            raise TypeError("The scalar must be a number")

        for i in range(self.shape):
            self.data[i] *= a

        return self

    def __add__(self, v: "Vector[K]") -> "Vector[K]":
        if not isinstance(v, Vector):
            return NotImplemented
        return Vector(self.data).add(v)

    def __sub__(self, v: "Vector[K]") -> "Vector[K]":
        if not isinstance(v, Vector):
            return NotImplemented
        return Vector(self.data).sub(v)

    def __mul__(self, s: 'K') -> "Vector[K]":
        if not _is_number(s):
            return NotImplemented
        return Vector(self.data).scl(s)

    __rmul__ = __mul__

    # Ex03
    def dot(self, v: 'Vector[k]') -> 'K':
        if self.shape != v.shape:
            raise ValueError("Vectors must have the same size")
        dt = 0
        for i in range(self.shape):
            dt += (self.data[i] * v.data[i])
        return dt

    # Ex04
    # Norme 1   : la somme des valeurs absolutes
    # Norme inf : max des valeurs
    # Norme     : sqrt(somme de |x_ij|^2)  (Frobenius)
    def norm_1(self) -> float:
        sm = 0.0
        for i in self.data:
            sm += _abs(i)
        return float(sm)

    def norm(self) -> float:
        sm = 0.0
        for i in self.data:
            a = _abs(i)
            sm += a ** 2
        return float(sm ** 0.5)

    def norm_inf(self) -> float:
        return float(max(_abs(i) for i in self.data))
