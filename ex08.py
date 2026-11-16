from src.matrice import Matrix
from src.complex import Complex

def test_trace():
    print("=== trace tests ===")

    A = Matrix([[1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0]])
    print(f"cas 1 (I3) : {A.trace()}")

    A = Matrix([[1.0, 2.0],
                [3.0, 4.0]])
    print(f"cas 2 : {A.trace()}")

    A = Matrix([[42.0]])
    print(f"cas 3 : {A.trace()}")

    A = Matrix([[8.0, 5.0, -2.0],
                [4.0, 7.0, 20.0],
                [7.0, 6.0, 1.0]])
    print(f"cas 4 : {A.trace()}")

    try:
        Matrix([[1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0]]).trace()
        print("cas 5 : ERREUR - aurait dû lever")
    except ValueError as e:
        print(f"cas 5 : {e}")

    A = Matrix([[1.0, 2.0],
                [3.0, 4.0]])
    B = Matrix([[5.0, 6.0],
                [7.0, 8.0]])
    lhs = A + B
    assert lhs.trace() == A.trace() + B.trace(), "Error"
    print(f"cas 6 : tr(A+B) = tr(A)+tr(B) = {lhs.trace()}")

    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0], [7.0, 8.0]])
    lhs = A.mul_mat(B).trace()
    rhs = B.mul_mat(A).trace()
    assert lhs == rhs, "Error"
    print(f"cas 7 : tr(AB) = tr(BA) = {lhs}")
    
    A = Matrix([[1, 2], [3, 4]])
    print(f"cas 8 : {A.trace()} (type={type(A.trace()).__name__})")

    A = Matrix([[1+2j, 0], [0, 3-1j]])
    print(f"cas 9 : {A.trace()} (type={type(A.trace()).__name__})")
    
    print(f"{'=' * 10}")
    u = Matrix([
        [1., 0.],
        [0., 1.],
    ])
    print(u.trace())

    u = Matrix([
        [2., -5., 0.],
        [4., 3., 7.],
        [-2., 3., 4.],
    ])
    print(u.trace())

    u = Matrix([
        [-2., -8., 4.],
        [1., -23., 4.],
        [0., 6., 4.],
    ])
    print(u.trace())

def test_trace_complex():
    print("=== trace tests Complex ===")
    A = Matrix([
        [Complex(1.0, 1.0), Complex(1.0, 1.0), Complex(1.0, 1.0)],
        [Complex(1.0, 1.0), Complex(1.0, 1.0), Complex(1.0, 1.0)],
        [Complex(1.0, 0.0), Complex(1.0, 0.0), Complex(1.0, 0.0)]
        ])
    print(A.trace())
    print('-----------')
    A = Matrix([
        [complex(1.0, 1.0), complex(1.0, 1.0), complex(1.0, 1.0)],
        [complex(1.0, 1.0), complex(1.0, 1.0), complex(1.0, 1.0)],
        [complex(1.0, 0.0), complex(1.0, 0.0), complex(1.0, 0.0)]
        ])
    print(A.trace())

def main():
    try:
        test_trace()
        test_trace_complex()

    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
