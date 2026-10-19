from numbers import Number
from src.vector import Vector, _is_number
from src.matrice import Matrix
from typing import TypeVar


K = TypeVar("K", bound=Number)
U = TypeVar("U", "Vector", "Matrix")
V = TypeVar("V", "Vector", "Matrix", complex, float)


# EX01
def linear_combination(u: list[U], coefs: list[K]) -> U:
    """This function calculates the linear combination"""
    if not u:
        raise ValueError("Do not give empty element")
    if not all(_is_number(x) for x in coefs):
        raise ValueError("Scalars must be numbers")
    if len(u) != len(coefs):
        raise ValueError("vectors and scalars should have same number")
    v = u[0].scl(coefs[0])
    for vec, coef in zip(u[1:], coefs[1:]):
        v.add(vec.scl(coef))
    return v

# Ex02
def lerp(u: V, v: V, t: float) -> V:
    """_summary_

    Args:
        u (V): _description_
        v (V): _description_
        t (float): _description_

    Raises:
        ValueError: _description_

    Returns:
        V: _description_
    """
    if not 0 <= t <= 1:
        raise ValueError("t should be between 0 and 1")
    if type(u) != type(v):
        raise ValueError("the two first paramters should have same type")
    if t == 0:
        return u
    if t == 1:
        return v
    return u + (v - u) * t

# Ex05
def angle_cos(u: 'U', v: 'U') -> float:
    """Cosine similarity between two vectors or two matrices."""
    if u.shape != v.shape:
        raise ValueError("Objects must have the same shape")

    norm_u = u.norm()
    norm_v = v.norm()
    if norm_u == 0.0 or norm_v == 0.0 :
        raise ValueError("Cosine is undefined for a zero vector")

    dot = u.dot(v)
    cos = float(dot / (norm_u * norm_v))
    return cos

# EX06
def cross_product(u: 'Vector[K]', v: 'Vector[K]') -> 'Vector[K]':
    """Calculate the cross produt of 3d Vector
       u = [u1, u2, u3]
       v = [v1, v2, v3]
       
                |u2 * v3 - u3 * v2|
       u . v =  |u3 * v1 - u1 * v3|
                |u1 * v2 - u2 * v1| 
    """
    if u.shape != 3 or v.shape != 3:
        raise ValueError("Both vectors should have the size of 3")

    u1, u2, u3 = u.data
    v1, v2, v3 = v.data

    cross = [u2 * v3 - u3 * v2,
             u3 * v1 - u1 * v3,
             u1 * v2 - u2 * v1]

    return Vector(cross)
