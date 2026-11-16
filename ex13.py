from src.matrice import Matrix
from src.complex import Complex


def show(name, A, expected):
    r = A.rank()
    status = "ok" if r == expected else f"FAUX (attendu {expected})"
    print(f"{name} : rank = {r}  [{status}]")


def test_rank():
    show("I3", Matrix([[1.0, 0.0, 0.0],
                       [0.0, 1.0, 0.0],
                       [0.0, 0.0, 1.0]]), 3)

    show("spec #1", Matrix([[1.0, 2.0, 0.0, 0.0],
                            [2.0, 4.0, 0.0, 0.0],
                            [-1.0, 2.0, 1.0, 1.0]]), 2)

    show("spec #2", Matrix([[8.0, 5.0, -2.0],
                            [4.0, 7.0, 20.0],
                            [7.0, 6.0, 1.0],
                            [21.0, 18.0, 7.0]]), 3)

    show("zéro 2x3", Matrix([[0.0, 0.0, 0.0],
                             [0.0, 0.0, 0.0]]), 0)

    show("doublon", Matrix([[1.0, 2.0],
                            [2.0, 4.0]]), 1)

    show("[[7]]", Matrix([[7.0]]), 1)

    show("[[0]]", Matrix([[0.0]]), 0)

    show("2x4", Matrix([[1.0, 2.0, 3.0, 4.0],
                        [5.0, 6.0, 7.0, 8.0]]), 2)

    A = Matrix([[1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0]])
    print(f"rank(A)  = {A.rank()}")
    print(f"rank(A^T) = {A.transpose().rank()}  (doit être égal)")
    
    A1 = Matrix([[Complex(1, 1), Complex(2, 2), Complex(3, 3)],
                [Complex(4, 4), Complex(5, 5), Complex(6, 6)]])
    print(f"rank(A1)  = {A.rank()}")
    A2 = Matrix([[complex(1, 1), complex(2, 2), complex(3, 3)],
                [complex(4, 4), complex(5, 5), complex(6, 6)]])
    print(f"rank(A2)  = {A2.rank()}")


def main():
    try:
        test_rank()

    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
