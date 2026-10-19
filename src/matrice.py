
from numbers import Number
from typing import Generic, TypeVar
from .vector import _is_number, Vector


K = TypeVar("K", bound=Number)


class Matrix(Generic[K]):
    """A rectangular matrix containing numeric elements."""
    def __init__(self, data: list[list[K]]):
        if not data:
            raise ValueError("A matrix cannot be empty")

        if not all(isinstance(row, list) for row in data):
            raise TypeError("Matrix data must contain lists")

        if not data[0]:
            raise ValueError("Matrix rows cannot be empty")

        columns = len(data[0])

        if not all(len(row) == columns for row in data):
            raise ValueError("All rows must have the same size")

        if not all(_is_number(x) for row in data for x in row):
            raise TypeError("Matrix elements must be numbers")

        self.data = [row.copy() for row in data]
        self.shape = (len(self.data), columns)

    def __repr__(self) -> str:
        return "\n".join(str(row) for row in self.data)

    def add(self, v: "Matrix[K]") -> "Matrix[K]":
        if self.shape != v.shape:
            raise ValueError("Matrices must have the same shape")

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.data[i][j] += v.data[i][j]

        return self

    def sub(self, v: "Matrix[K]") -> "Matrix[K]":
        if self.shape != v.shape:
            raise ValueError("Matrices must have the same shape")

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.data[i][j] -= v.data[i][j]

        return self

    def scl(self, a: K) -> "Matrix[K]":
        if not _is_number(a):
            raise TypeError("The scalar must be a number")

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.data[i][j] *= a

        return self

    def __add__(self, v: 'Matrix[K]')-> "Matrix[K]":
        if not isinstance(v, Matrix):
            raise NotImplemented
        return Matrix(self.data).add(v)

    def __sub__(self, v: 'Matrix[K]')-> "Matrix[K]":
        if not isinstance(v, Matrix):
            raise NotImplemented
        return Matrix(self.data).sub(v)

    def __mul__(self, s: "K")-> "Matrix[K]":
        if not _is_number(s):
            return NotImplemented
        return Matrix(self.data).scl(s)

    # Ex03
    # Frobenius
    def dot(self, v: 'Matrix[K]') -> 'K':
        if self.shape != v.shape:
            raise ValueError("Matrix must have the same size")
        dt = 0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                dt += (v.data[i][j] * self.data[i][j])    
        return dt

    # Ex04
    # Norme 1   : max des sommes de |colonnes|
    # Norme inf : max des sommes de |lignes|
    # Norme     : sqrt(somme de |x_ij|^2)  (Frobenius)

    def norm_1(self) -> float:
        mx = 0.0
        for j in range(self.shape[1]):
            sm = 0.0
            for i in range(self.shape[0]):
                sm += abs(self.data[i][j])
            if sm > mx:
                mx = sm
        return float(mx)

    def norm(self) -> float:
        sm = 0.0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                a = abs(self.data[i][j])
                sm += a * a
        return float(sm ** 0.5)

    def norm_inf(self) -> float:
        mx = 0.0
        for i in range(self.shape[0]):
            sm = 0.0
            for j in range(self.shape[1]):
                sm += abs(self.data[i][j])
            if sm > mx:
                mx = sm
        return float(mx)

    # Ex07
    def mul_vec(self, vec: 'Vector[K]') -> 'Vector[K]':
        """Multiply this matrix by a vector.

            Computes y = A · x, where A is `self` (m x n) and x is `vec`
            (n elements):

                y[i] = sum_{j=1..n} A[i][j] * x[j]
                    for i = 1..m
        """
        
        if self.shape[1] != vec.shape:
            raise ValueError("Matrix columns and vector size must match")

        result = []
        for i in range(self.shape[0]):
            row = Vector(self.data[i])
            result.append(row.dot(vec))
        return Vector(result)
                

    def mul_mat(self, mat: 'Matrix[K]') -> 'Matrix[K]':
        """ Multiply this matrix by another matrix.

            Computes C = A · B, where A is `self` (m x n) and B is `mat` (n x p):

            C[i][j] = sum_{k=1..n} A[i][k] * B[k][j]
                for i = 1..m, j = 1..p
        """
        
        if self.shape[1] != mat.shape[0]:
            raise ValueError("Matrix 1 columns and Matrix 2 rows must match")
        mx = []
        for i in range(self.shape[0]):
            v = []
            for j in range(mat.shape[1]):
                dot =0
                for z in range(mat.shape[0]):
                    dot += self.data[i][z] * mat.data[z][j]
                v.append(dot)
            mx.append(v)
        return Matrix(mx)
