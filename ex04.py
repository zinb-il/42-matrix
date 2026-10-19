from src.vector import Vector
from src.matrice import Matrix

def test_vector_norms():
    print("=== Vector norms ===")

    u = Vector([0.0, 0.0, 0.0])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # Attendu : 0.0, 0.0, 0.0

    u = Vector([1.0, 2.0, 3.0])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # Attendu : 6.0, 3.74165738, 3.0

    u = Vector([-1.0, -2.0])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # Attendu : 3.0, 2.236067977, 2.0


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


def main():
    try:
        test_vector_norms()
        test_matrix_norms()

    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"Error exception {err} \nline: {err.__traceback__.tb_lineno}")


if __name__ == "__main__":
    main()
