from src.vector import Vector
from src.matrice import Matrix
from src.complex import Complex


def main():
    try:
        # Frobenius Dot scalar
        # Vector tests
        print("\n=== Vector tests ===")
        u = Vector([0., 0.])
        v = Vector([1., 1.])
        print(u.dot(v))

        u = Vector([1., 1.])
        v = Vector([1., 1.])
        print(u.dot(v))

        u = Vector([-1., 6.])
        v = Vector([3., 2.])
        print(u.dot(v))
        
        print("\n=== Complex Vector tests ===")
        cu = Vector([Complex(1, 1), Complex(2, 0)])
        cv = Vector([Complex(1, -1), Complex(0, 2)])
        cu1 = Vector([1 + 1j, 2 + 0j])
        cv1 = Vector([1 - 1j, 2j])
        print(cu.dot(cv))  
        print(f"{'-' * 5}")
        print(cu1.dot(cv1))
        print(f"{'-' * 5}")
        mixed = Vector([Complex(2, 0), Complex(0, 3), 4])
        other = Vector([Complex(1, 0), Complex(1, 1), 2.])
        mixed1 = Vector([complex(2, 0), complex(0, 3), 4])
        other1 = Vector([complex(1, 0), complex(1, 1), 2.0])
        print(mixed.dot(other))
        print(f"{'-' * 5}")
        print(mixed1.dot(other1))

        # Matrix tests
        print("\n=== Matrix tests ===")
        u = Matrix([[4, 2], [0, 3]])
        v = Matrix([[4, 0], [1, 4]])
        print(u.dot(v))
        print("\n=== Complex Matrix tests ===")
        cm_u = Matrix([
            [Complex(4, 0), Complex(2, 1)],
            [Complex(0, -1), Complex(3, 0)],
        ])
        cm_v = Matrix([
            [Complex(4, 0), Complex(0, 0)],
            [Complex(1, 0), Complex(4, 2)],
        ])
        print(cm_u.dot(cm_v))
        cm_u = Matrix([
            [complex(4, 0), complex(2, 1)],
            [complex(0, -1), complex(3, 0)],
        ])
        cm_v = Matrix([
            [complex(4, 0), complex(0, 0)],
            [complex(1, 0), complex(4, 2)],
        ])
        print(f"{'-' * 5}")
        print(cm_u.dot(cm_v))
        
        # Invalid Tests
        print("\n=== Error tests ===")
        try:
            u = Vector([-1., 6.])
            u.dot(Vector([1])) 
        except Exception as err:
            print(err)

    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"Error exception {err} \nline: {err.__traceback__.tb_lineno}")


if __name__ == "__main__":
    main()
