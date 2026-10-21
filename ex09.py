from src.matrice import Matrix

def test_transpose():
    print("=== transpose tests ===")


    A = Matrix([[1.0, 0.0],
                [0.0, 1.0]])
    print("cas 1 :")
    print(A.transpose())


    A = Matrix([[1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0]])
    print("cas 2 (attendu [[1,4],[2,5],[3,6]]) :")
    print(A.transpose())

    A = Matrix([[1.0],
                [2.0],
                [3.0]])
    print("cas 3 (attendu [[1,2,3]]) :")
    print(A.transpose())

    A = Matrix([[1.0, 2.0, 3.0, 4.0]])
    print("cas 4 (attendu [[1],[2],[3],[4]]) :")
    print(A.transpose())

    A = Matrix([[1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.0, 9.0]])
    print("cas 5 :")
    print(A.transpose())

    A = Matrix([[1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0]])
    assert A.transpose().transpose().data == A.data, "Assertion err"
    print("cas 6 : (A^T)^T = A")

    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0], [7.0, 8.0]])
    lhs = (A + B).transpose().data
    rhs = Matrix(A.transpose().data).add(B.transpose()).data
    assert lhs == rhs, "Assertion err"
    print("cas 7 : (A+B)^T = A^T+B^T")

    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0], [7.0, 8.0]])
    lhs = A.mul_mat(B).transpose().data
    rhs = B.transpose().mul_mat(A.transpose()).data
    assert lhs == rhs, "Assertion err"
    print("cas 8 : (AB)^T = B^T A^T")

    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    A.transpose()
    assert A.data == [[1.0, 2.0], [3.0, 4.0]], "self muté !"
    print("cas 9 : ok, self non muté")

    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    assert A.trace() == A.transpose().trace(), "Assertion err"
    print("cas 10 : tr(A^T) = tr(A)")

def main():
    try:
        test_transpose()

    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
