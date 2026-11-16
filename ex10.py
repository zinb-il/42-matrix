from src.matrice import Matrix
from src.complex import Complex

def test_row_echelon():
    print("=== row_echelon tests ===")

    A = Matrix([[1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0]])
    print("cas 1 :")
    print(A.row_echelon(),"\n")


    A = Matrix([[1.0, 2.0],
                [3.0, 4.0]])
    print("cas 2 (attendu I2(matrice d'identité)) :")
    print(A.row_echelon(),"\n")

    A = Matrix([[1.0, 2.0],
                [2.0, 4.0]])
    print("cas 3 (attendu [[1,2],[0,0]]) :")
    print(A.row_echelon(),"\n")

    A = Matrix([
        [8.0, 5.0, -2.0, 4.0, 28.0],
        [4.0, 2.5, 20.0, 4.0, -4.0],
        [8.0, 5.0, 1.0, 4.0, 17.0],
    ])
    print("cas 4 (REF attendue de la spec) :")
    print(A.row_echelon(),"\n")

    A = Matrix([[0.0, 0.0],
                [1.0, 2.0]])
    print("cas 5 (attendu [[1,2],[0,0]]) :")
    print(A.row_echelon(),"\n")

    A = Matrix([[0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0]])
    print("cas 6 (attendu [[0,0,0],[0,0,0]]) :")
    print(A.row_echelon(),"\n")

    A = Matrix([[42.0]])
    print("cas 7 (attendu [[1]]) :")
    print(A.row_echelon(),"\n")
    
    A = Matrix([[1,2,1,0],[3,4,0,1]])
    print("cas 8 :")
    print(A.row_echelon(),"\n")
    
def test_row_echelon_complex():
    print("=== row_echelon tests Complex ===")

    A = Matrix([[Complex(1, 1), Complex(0, 1), Complex(1, 0)],
                [Complex(2, 2), Complex(0, 2), Complex(2, 0)],
                [Complex(3, 3), Complex(0, 3), Complex(3, 0)]])
    A1 = Matrix([[complex(1, 1), complex(0, 1), complex(1, 0)],
                [complex(2, 2), complex(0, 2), complex(2, 0)],
                [complex(3, 3), complex(0, 3), complex(3, 0)]])
    print("cas 1 :")
    print(A.row_echelon(),"\n")
    print('------')
    print(A1.row_echelon())
    print('----------------------------------')


    A = Matrix([[Complex(1, 1), Complex(2, 2)],
                [Complex(3, 3), Complex(4, 4)]])
    A1 = Matrix([[complex(1, 1), complex(2, 2)],
                [complex(3, 3), complex(4, 4)]])
    print("cas 2222:")
    print(A.row_echelon(),"\n")
    print('------')
    print(A1.row_echelon())

def main():
    try:
        test_row_echelon()
        test_row_echelon_complex()

    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
