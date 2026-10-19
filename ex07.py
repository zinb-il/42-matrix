from src.vector import Vector
from src.matrice import Matrix


def test_mul_vec():
    print("=== mul_vec tests ===")

    A = Matrix([[1.0, 0.0], [0.0, 1.0]])
    x = Vector([4.0, 2.0])
    print("cas 1 :")
    print(A.mul_vec(x))

    A = Matrix([[2.0, 0.0], [0.0, 2.0]])
    x = Vector([4.0, 2.0])
    print("cas 2 :")
    print(A.mul_vec(x))

    A = Matrix([[2.0, -2.0], [-2.0, 2.0]])
    x = Vector([4.0, 2.0])
    print("cas 3 :")
    print(A.mul_vec(x))

    try:
        Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]).mul_vec(Vector([1.0, 2.0]))
        print("cas 4 : ERREUR - aurait dû lever")
    except ValueError as e:
        print(f"cas 4 : ({e})")

    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    x = Vector([1.0, 1.0])
    A.mul_vec(x)
    assert x.data == [1.0, 1.0], "x a été muté !"
    print("cas 5 : entrée non mutée")


def test_mul_mat():
    print("=== mul_mat tests ===")

    A = Matrix([[1.0, 0.0], [0.0, 1.0]])
    B = Matrix([[1.0, 0.0], [0.0, 1.0]])
    print("cas 1 :")
    print(A.mul_mat(B))

    A = Matrix([[1.0, 0.0], [0.0, 1.0]])
    B = Matrix([[2.0, 1.0], [4.0, 2.0]])
    print("cas 2 :")
    print(A.mul_mat(B))

    A = Matrix([[3.0, -5.0], [6.0, 8.0]])
    B = Matrix([[2.0, 1.0], [4.0, 2.0]])
    print("cas 3 :")
    print(A.mul_mat(B))

    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[1.0, 0.0], [0.0, 1.0]])
    print("cas 4 (A x I doit redonner A) :")
    print(A.mul_mat(B))

    try:
        Matrix([[1.0, 2.0]]).mul_mat(Matrix([[1.0, 2.0]]))
        print("cas 5 : ERREUR - aurait dû lever")
    except ValueError as e:
        print(f"cas 5 : {e}")

    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0], [7.0, 8.0]])
    A.mul_mat(B)
    assert A.data == [[1.0, 2.0], [3.0, 4.0]], "A a été muté !"
    assert B.data == [[5.0, 6.0], [7.0, 8.0]], "B a été muté !"
    print("cas 6 : entrées non mutées")

    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0], [7.0, 8.0]])
    C = Matrix([[9.0, 10.0], [11.0, 12.0]])
    assert (A.mul_mat(B)).mul_mat(C).data == A.mul_mat(B.mul_mat(C)).data
    print("cas 7 : associativité vérifiée")

    A = Matrix([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
    ])
    B = Matrix([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
    ])
    print("cas 8 (2x3 x 3x4) :")
    print(A.mul_mat(B)) 

def main():
    try:
        test_mul_vec()
        test_mul_mat()

    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
