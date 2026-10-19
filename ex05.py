from src.vector import Vector
from src.matrice import Matrix
from src.functions import angle_cos


def test_angle_cos_vectors():
    print("=== angle_cos tests for vectors ===")

    u = Vector([1.0, 0.0])
    v = Vector([1.0, 0.0])
    print(f"cas 1 : {angle_cos(u, v)}")

    u = Vector([1.0, 0.0])
    v = Vector([0.0, 1.0])
    print(f"cas 2 : {angle_cos(u, v)}")

    u = Vector([-1.0, 1.0])
    v = Vector([1.0, -1.0])
    print(f"cas 3 : {angle_cos(u, v)}")

    u = Vector([2.0, 1.0])
    v = Vector([4.0, 2.0])
    print(f"cas 4 : {angle_cos(u, v)}")


    u = Vector([1.0, 2.0, 3.0])
    v = Vector([4.0, 5.0, 6.0])
    print(f"cas 5 : {angle_cos(u, v)}")

    try:
        angle_cos(Vector([1.0, 2.0]), Vector([1.0, 2.0, 3.0]))
    except ValueError as e:
        print(f"cas 6 : ({e})")

    try:
        angle_cos(Vector([0.0, 0.0]), Vector([1.0, 0.0]))
    except ValueError as e:
        print(f"cas 7 : {e})")
        
def test_angle_cos_matrixs():
    try:
        print("=== angle_cos tests for matrixs ===")
        A = Matrix([[1.0, 2.0], [3.0, 4.0]])
        B = Matrix([[1.0, 2.0], [3.0, 4.0]])
        print(angle_cos(A, B))

        C = Matrix([[4.0, 3.0], [2.0, 1.0]])
        print(angle_cos(A, C))

        D = Matrix([[-1.0, -2.0], [-3.0, -4.0]])
        print(angle_cos(A, D))

    except Exception as err:
        print(f"Unexpected error: {err}")

def main():
    try:
        test_angle_cos_vectors()
        test_angle_cos_matrixs()

    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
