from src.vector import Vector, _is_number
from src.matrice import Matrix
from src.complex import Complex
from src.functions import lerp


def main():
    try:
        # Scalar tests
        print("\n=== Scalar tests ===")
        print(lerp(0., 1., 0.))
        print(lerp(0., 1., 1.))
        print(lerp(0., 1., 0.5))
        print(lerp(21., 42., 0.3))
        
        print("\n=== Complex Scalar tests ===")
        print(lerp(Complex(0, 0), Complex(1, 1), 0.5))
        print(lerp(Complex(0, 0), Complex(1, 1), 1.))
        
        # Vector tests
        print("\n=== Vector tests ===")
        print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3))
        print(f"{'-' * 5}")
        print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0))
        print(f"{'-' * 5}")
        print(lerp(Vector([2., 1.]), Vector([4., 2.]), 1))
        
        print("\n=== Complex Vector tests ===")
        cu = Vector([Complex(2, 1), Complex(0, -1)])
        cv = Vector([Complex(4, -1), Complex(2, 3)])
        cu1 = Vector([complex(2, 1), complex(0, -1)])
        cv1 = Vector([complex(4, -1), complex(2, 3)])
        print(lerp(cu, cv, 0.3))
        print(f"{'-' * 5}")
        print(lerp(cu1, cv1, 0.3))
        print(f"{'-' * 50}")

        print(lerp(cu, cv, 0))
        print(f"{'-' * 5}")
        print(lerp(cu1, cv1, 0))
        print(f"{'-' * 50}")

        print(lerp(cu, cv, 1))
        print(f"{'-' * 5}")
        print(lerp(cu1, cv1, 1))
        print(f"{'-' * 50}")

        # Matrix tests
        print("\n=== Matrix tests ===")
        print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20.,10.], [30., 40.]]), 0.5))
        
        print("\n=== Complex Matrix tests ===")
        cm_u = Matrix([
            [Complex(2, 0), Complex(1, 1)],
            [Complex(3, -1), Complex(4, 0)],
        ])
        cm_v = Matrix([
            [Complex(20, 2), Complex(10, -2)],
            [Complex(30, 0), Complex(40, 4)],
        ])
        cm_u1 = Matrix([
            [complex(2, 0), complex(1, 1)],
            [complex(3, -1), complex(4, 0)],
        ])
        cm_v1 = Matrix([
            [complex(20, 2), complex(10, -2)],
            [complex(30, 0), complex(40, 4)],
        ])
        print(lerp(cm_u, cm_v, 0.5))
        print(f"{'-' * 5}")
        print(lerp(cm_u1, cm_v1, 0.5))
        
        # Invalid Tests
        print("\n=== Error tests ===")
        try:
            lerp(Vector([1,2]), Vector([2]), 5)   
        except Exception as err:
            print(err)
        try:
            lerp(Vector([1,2]), 2, 0)   
        except Exception as err:
            print(err)    
        try:
            print(lerp(Matrix([[2., 1.], [3., 4.]]), Vector([1,2]), 0.5))   
        except Exception as err:
            print(err)

    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"Error exception {err} \nline: {err.__traceback__.tb_lineno}")


if __name__ == "__main__":
    main()
