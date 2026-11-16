from src.vector import Vector
from src.matrice import Matrix
from src.complex import Complex
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

def test_angle_cos_vectors_complex():
    print("=== angle_cos tests for vectors (complex) ===")

    u = Vector([Complex(1.0, 0.0), Complex(0.0, 0.0)])
    v = Vector([Complex(0.0, 0.0), Complex(0.0, 1.0)])
    res = angle_cos(u, v)
    print(res)
    uc = Vector([1+0j, 0+0j])
    vc = Vector([0+0j, 0+1j])
    print(f"{'-'* 5 }")
    print(angle_cos(uc, vc))
    
    u = Vector([Complex(1.0, 0.0), Complex(1.0, 1.0)])
    v = Vector([
        Complex(1.0, 1.0) * Complex(1.0, 0.0),
        Complex(1.0, 1.0) * Complex(1.0, 1.0),
    ])
    res = angle_cos(u, v)
    print(res)
    uc = Vector([1+0j, 1+1j])
    vc = Vector([(1+1j)*(1+0j), (1+1j)*(1+1j)])
    print(f"{'-'* 5 }")
    print(angle_cos(uc, vc))


def test_angle_cos_matrixs_complex():
    print("=== angle_cos tests for matrixs (complex) ===")


    A = Matrix([
        [Complex(1.0, 0.0), Complex(0.0, 0.0)],
        [Complex(0.0, 0.0), Complex(0.0, 0.0)],
    ])
    B = Matrix([
        [Complex(0.0, 0.0), Complex(0.0, 0.0)],
        [Complex(0.0, 0.0), Complex(1.0, 0.0)],
    ])
    res = angle_cos(A, B)
    print(res)
    Ac = Matrix([[1+0j, 0+0j], [0+0j, 0+0j]])
    Bc = Matrix([[0+0j, 0+0j], [0+0j, 1+0j]])
    print(f"{'-'* 5 }")
    print(angle_cos(Ac, Bc))
    print(f"{'-'* 5 }")

    A = Matrix([
        [Complex(1.0, 0.0), Complex(2.0, 1.0)],
        [Complex(3.0, -1.0), Complex(4.0, 0.0)],
    ])
    k = Complex(1.0, 1.0)
    B = Matrix([
        [k * Complex(1.0, 0.0), k * Complex(2.0, 1.0)],
        [k * Complex(3.0, -1.0), k * Complex(4.0, 0.0)],
    ])
    res = angle_cos(A, B)
    print(res)
    Ac = Matrix([[1+0j, 2+1j], [3-1j, 4+0j]])
    kc = 1+1j
    Bc = Matrix([[kc*(1+0j), kc*(2+1j)], [kc*(3-1j), kc*(4+0j)]])
    print(f"{'-'* 5 }")
    print(angle_cos(Ac, Bc))
    

def main():
    try:
        test_angle_cos_vectors()
        test_angle_cos_matrixs()
        test_angle_cos_vectors_complex()
        test_angle_cos_matrixs_complex()

    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
