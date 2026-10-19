from typing import TypeVar
from src.vector import Vector
from src.functions import cross_product


def test_cross_product():
    print("=== cross_product tests ===")

    u = Vector([0.0, 0.0, 1.0])
    v = Vector([1.0, 0.0, 0.0])
    print("cas 1 :")
    print(cross_product(u, v))

    u = Vector([1.0, 2.0, 3.0])
    v = Vector([4.0, 5.0, 6.0])
    print("cas 2 :")
    print(cross_product(u, v))

    u = Vector([4.0, 2.0, -3.0])
    v = Vector([-2.0, -5.0, 16.0])
    print("cas 3 :")
    print(cross_product(u, v))

    u = Vector([1.0, 2.0, 3.0])
    v = Vector([4.0, 5.0, 6.0])
    print("cas 4 (u×v + v×u doit être nul) :")
    w1 = cross_product(u, v)
    w2 = cross_product(v, u)
    print(w1 + w2)

    u = Vector([1.0, 2.0, 3.0])
    print("cas 5 (u × u) :")
    print(cross_product(u, u))

    z = Vector([0.0, 0.0, 0.0])
    v = Vector([1.0, 2.0, 3.0])
    print("cas 6 (0 × v) :")
    print(cross_product(z, v))

    try:
        cross_product(Vector([1.0, 2.0]), Vector([1.0, 2.0, 3.0]))
    except ValueError as e:
        print(f"cas 7 : ({e})")

    u = Vector([1.0, 2.0, 3.0])
    v = Vector([4.0, 5.0, 6.0])
    w = cross_product(u, v)
    print(f"cas 8 : u·w = {u.dot(w)}, v·w = {v.dot(w)}")  # 0.0, 0.0
        

def main():
    try:
        test_cross_product()

    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
