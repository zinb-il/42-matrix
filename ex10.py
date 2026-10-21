from src.matrice import Matrix

def test_row_echelon():
    print("=== row_echelon tests ===")

    A = Matrix([[1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0]])
    print("cas 1 :")
    print(A.row_echelon())


    A = Matrix([[1.0, 2.0],
                [3.0, 4.0]])
    print("cas 2 (attendu I2) :")
    print(A.row_echelon())

    A = Matrix([[1.0, 2.0],
                [2.0, 4.0]])
    print("cas 3 (attendu [[1,2],[0,0]]) :")
    print(A.row_echelon())

    A = Matrix([
        [8.0, 5.0, -2.0, 4.0, 28.0],
        [4.0, 2.5, 20.0, 4.0, -4.0],
        [8.0, 5.0, 1.0, 4.0, 17.0],
    ])
    print("cas 4 (REF attendue de la spec) :")
    print(A.row_echelon())

    A = Matrix([[0.0, 0.0],
                [1.0, 2.0]])
    print("cas 5 (attendu [[1,2],[0,0]]) :")
    print(A.row_echelon())

    A = Matrix([[0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0]])
    print("cas 6 (attendu [[0,0,0],[0,0,0]]) :")
    print(A.row_echelon())

    A = Matrix([[42.0]])
    print("cas 7 (attendu [[1]]) :")
    print(A.row_echelon())

    # # 8. Vérification : les pivots sont 1 et les zéros sous les pivots
    # A = Matrix([
    #     [2.0, 4.0, 6.0],
    #     [1.0, 3.0, 5.0],
    #     [3.0, 7.0, 9.0],
    # ])
    # R = A.row_echelon()
    # print("cas 8 (vérif structure) :")
    # print(R)
    # for i in range(R.shape[0]):
    #     for j in range(R.shape[1]):
    #         if R.data[i][j] != 0:
    #             assert R.data[i][j] == 1.0 or True
    #             break

    # A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    # A.row_echelon()
    # assert A.data == [[1.0, 2.0], [3.0, 4.0]], "self muté !"
    # print("cas 9 : self non muté")

    # A = Matrix([
    #     [1.0, 2.0, 3.0],
    #     [4.0, 5.0, 6.0],
    #     [7.0, 8.0, 9.0],
    # ])
    # R = A.row_echelon()
    # rank = sum(1 for row in R.data if any(x != 0 for x in row))
    # print(f"cas 10 : rang = {rank} (attendu 2 car 3e ligne = combinaison des 2 premières)")

def main():
    try:
        test_row_echelon()

    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
