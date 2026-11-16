from src.vector import Vector, _abs
from src.matrice import Matrix
from src.complex import Complex

def test_vector_norms():
    print("=== Vector norms ===")

    u = Vector([0.0, 0.0, 0.0])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")

    u = Vector([1.0, 2.0, 3.0])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")

    u = Vector([-1.0, -2.0])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")


def test_vector_norms_complex():
    print("\n=== Vector norms (Complex) ===")

    cu = Vector([Complex(1, 2), Complex(3, -4), Complex(0, 0)])
    ref = [complex(1, 2), complex(3, -4), complex(0, 0)]

    n1_expected = sum(abs(z) for z in ref)
    n2_expected = sum(abs(z) ** 2 for z in ref) ** 0.5
    ninf_expected = max(abs(z) for z in ref)

    n1_got = cu.norm_1()
    n2_got = cu.norm()
    ninf_got = cu.norm_inf()

    print(f"mine : {n1_got}, {n2_got}, {ninf_got}")
    print(f"ref  : {n1_expected}, {n2_expected}, {ninf_expected}")
    print(f"{'-' * 20}")


    # Vecteur complexe pur imaginaire : u = (i, -2i, 3i)
    cu2 = Vector([Complex(0, 1), Complex(0, -2), Complex(0, 3)])
    ref2 = [complex(0, 1), complex(0, -2), complex(0, 3)]
    print(f"mine : {cu2.norm_1()}, {cu2.norm()}, {cu2.norm_inf()}")
    print(f"ref  : "
          f"{sum(abs(z) for z in ref2)}, "
          f"{sum(abs(z) ** 2 for z in ref2) ** 0.5}, "
          f"{max(abs(z) for z in ref2)}")
    print(f"{'-' * 20}")

    # Vecteur mixte réel/complexe
    cu3 = Vector([1, Complex(0, 1), 3.0, Complex(4, -4)])
    ref3 = [complex(1, 0), complex(0, 1), complex(3, 0), complex(4, -4)]
    print(f"mine : {cu3.norm_1()}, {cu3.norm()}, {cu3.norm_inf()}")
    print(f"ref  : "
          f"{sum(abs(z) for z in ref3)}, "
          f"{sum(abs(z) ** 2 for z in ref3) ** 0.5}, "
          f"{max(abs(z) for z in ref3)}")


def test_matrix_norms():
    print("\n=== Matrix norms ===")

    # Matrice [[1, 2], [3, 4]]
    m = Matrix([[1.0, 2.0], [3.0, 4.0]])
    print(f"norm_1   = {m.norm_1()}")
    print(f"norm_inf = {m.norm_inf()}")
    print(f"norm     = {m.norm()}")

    # Matrice [[0, 0], [0, 0]]
    m0 = Matrix([[0.0, 0.0], [0.0, 0.0]])
    print(f"zero matrix: {m0.norm_1()}, {m0.norm_inf()}, {m0.norm()}")
    # Attendu : 0.0, 0.0, 0.0


def test_matrix_norms_complex():
    print("\n=== Matrix norms (Complex) ===")

    # M = [[1+i, 2], [3i, 4-4i]]
    cm = Matrix([
        [Complex(1, 1), Complex(2, 0)],
        [Complex(0, 3), Complex(4, -4)],
    ])
    ref = [
        [complex(1, 1), complex(2, 0)],
        [complex(0, 3), complex(4, -4)],
    ]

    # Frobenius (norm) : sqrt(Σ |a_ij|^2)
    frob_expected = sum(abs(z) ** 2 for row in ref for z in row) ** 0.5

    # norm_1 (induite) : max sur les colonnes de Σ |a_ij|
    n1_expected = max(
        sum(abs(ref[i][j]) for i in range(len(ref)))
        for j in range(len(ref[0]))
    )

    # norm_inf (induite) : max sur les lignes de Σ |a_ij|
    ninf_expected = max(
        sum(abs(ref[i][j]) for j in range(len(ref[0])))
        for i in range(len(ref))
    )

    n1_got = cm.norm_1()
    ninf_got = cm.norm_inf()
    frob_got = cm.norm()

    print(f"mine : norm_1={n1_got}, norm_inf={ninf_got}, norm={frob_got}")
    print(f"ref  : norm_1={n1_expected}, norm_inf={ninf_expected}, norm={frob_expected}")
    print(f"{'-' * 20}")

 

    # Matrice complexe purement imaginaire
    cm2 = Matrix([
        [Complex(0, 1), Complex(0, -2)],
        [Complex(0, 3), Complex(0, 0.5)],
    ])
    ref2 = [
        [complex(0, 1), complex(0, -2)],
        [complex(0, 3), complex(0, 0.5)],
    ]
    print(f"mine : {cm2.norm_1()}, {cm2.norm_inf()}, {cm2.norm()}")
    print(f"ref  : "
          f"{max(sum(abs(ref2[i][j]) for i in range(2)) for j in range(2))}, "
          f"{max(sum(abs(ref2[i][j]) for j in range(2)) for i in range(2))}, "
          f"{sum(abs(z) ** 2 for row in ref2 for z in row) ** 0.5}")


def main():
    try:
        test_vector_norms()
        test_matrix_norms()
        test_vector_norms_complex()
        test_matrix_norms_complex()

    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"Error exception {err} \nline: {err.__traceback__.tb_lineno}")


if __name__ == "__main__":
    main()
