from src.matrice import Matrix

def test_determinant():
    print("=== determinant tests ===")

    A = Matrix([[1.0, -1.0],
                [-1.0, 1.0]])
    print(f"cas 1 (attendu 0) : {A.determinant()}")

    A = Matrix([[2.0, 0.0, 0.0],
                [0.0, 2.0, 0.0],
                [0.0, 0.0, 2.0]])
    print(f"cas 2 (attendu 8) : {A.determinant()}")

    A = Matrix([[8.0, 5.0, -2.0],
                [4.0, 2.5, 20.0],
                [8.0, 5.0, 1.0]])
    print(f"cas 3 (attendu 0) : {A.determinant()}")

    A = Matrix([[8.0, 5.0, -2.0, 4.0],
                [4.0, 2.5, 20.0, 4.0],
                [8.0, 5.0, 1.0, 4.0],
                [28.0, -4.0, 17.0, 1.0]])
    print(f"cas 4 (attendu 1032) : {A.determinant()}")

    for n in (1, 2, 3, 4):
        I = Matrix([[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)])
        print(f"cas 5 (I{n}) : {I.determinant()}")


    A = Matrix([[42.0]])
    print(f"cas 6 (attendu 42) : {A.determinant()}")

    A = Matrix([[1e-15]])
    print(f"cas 7 (attendu 1e-15) : {A.determinant()}")

    try:
        Matrix([[1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0]]).determinant()
        print("cas 8 : ERREUR - aurait dû lever")
    except ValueError as e:
        print(f"cas 8 : {e}")

    A = Matrix([[3.0, 8.0],
                [4.0, 6.0]])
    assert A.determinant() == A.transpose().determinant()
    print(f"cas 9 : det(A^T) = det(A) = {A.determinant()}")

    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0], [7.0, 8.0]])
    lhs = A.mul_mat(B).determinant()
    rhs = A.determinant() * B.determinant()
    assert abs(lhs - rhs) < 1e-9, f"{lhs} != {rhs}"
    print(f"cas 10 : det(AB) = det(A)det(B) = {lhs}")

    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    A.determinant()
    assert A.data == [[1.0, 2.0], [3.0, 4.0]], "self muté !"
    print("cas 11 : ok, self non muté")

    A = Matrix([[1 + 5j, 2 + 1j], [3, 4]])
    d = A.determinant()
    print(f"cas 12 : det = {d} (type={type(d).__name__})")

    A = Matrix([[4.0, 3.0],
                [1.0, 2.0]])
    print(f"cas 13 (attendu 0) : {A.determinant()}")

def main():
    try:
        test_determinant()

    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
