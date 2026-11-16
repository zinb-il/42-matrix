from src.vector import Vector
from src.matrice import Matrix
from src.complex import Complex
from src.functions import linear_combination


def main():
    try:
        # Vector tests
        print("\n=== Vector tests ===")
        e1 = Vector([1., 0., 0.])
        e2 = Vector([0., 1., 0.])
        e3 = Vector([0., 0., 1.])
        v1 = Vector([1., 2., 3.])
        v2 = Vector([0., 10., -100.])
        print(linear_combination([e1, e2, e3], [10., -2., 0.5]))
        print(f"{'-' * 50}")
        v1 = Vector([1., 2., 3.])
        v2 = Vector([0., 10., -100.])
        print(linear_combination([v1, v2], [10., -2.]))
        
        print("\n=== Complex Vector tests ===")
        ce1 = Vector([Complex(1, 0), Complex(0, 0), Complex(0, 0)])
        ce2 = Vector([Complex(0, 0), Complex(1, 0), Complex(0, 0)])
        ce3 = Vector([Complex(0, 0), Complex(0, 0), Complex(1, 0)])
        ccoefs = [Complex(10, 1), Complex(-2, 3), Complex(0.5, -0.5)]
        print(linear_combination([ce1, ce2, ce3], ccoefs))
        print(f"{'-' * 10}")
        ce1 = Vector([complex(1, 0), complex(0, 0), complex(0, 0)])
        ce2 = Vector([complex(0, 0), complex(1, 0), complex(0, 0)])
        ce3 = Vector([complex(0, 0), complex(0, 0), complex(1, 0)])
        ccoefs = [complex(10, 1), complex(-2, 3), complex(0.5, -0.5)]
        print(linear_combination([ce1, ce2, ce3], ccoefs))
        print(f"{'-' * 50}")
        
        cv1 = Vector([Complex(1, 2), Complex(3, -1), Complex(0, 4)])
        cv2 = Vector([Complex(0, -1), Complex(10, 0), Complex(-100, 5)])
        print(linear_combination([cv1, cv2], [10., -2.]))
        print(f"{'-' * 10}")
        cv1 = Vector([complex(1, 2), complex(3, -1), complex(0, 4)])
        cv2 = Vector([complex(0, -1), complex(10, 0), complex(-100, 5)])
        print(linear_combination([cv1, cv2], [10., -2.]))
        print(f"{'-' * 50}")
        
        print(linear_combination(
            [Vector([Complex(1, 1), Complex(2, 0)]),
             Vector([Complex(0, -1), Complex(3, 2)])],
            [2, 0.5]
        ))
        print(f"{'-' * 10}")
        print(linear_combination(
            [Vector([complex(1, 1), complex(2, 0)]),
             Vector([complex(0, -1), complex(3, 2)])],
            [2, 0.5]
        ))


        # Matrix tests
        print("\n=== Matrix tests ===")
        m1 = Matrix([[1., 0., 0.], [0., 1., 0.]])
        m2 = Matrix([[1., 0., 0.], [0., 1., 0.]])
        print(linear_combination([m1, m2], [10., -2.]))
        
        print("\n=== Complex Matrix tests ===")
        cm1 = Matrix([
            [Complex(1, 1), Complex(0, 0), Complex(0, 0)],
            [Complex(0, 0), Complex(1, -1), Complex(0, 0)],
        ])
        cm2 = Matrix([
            [Complex(0, -1), Complex(0, 0), Complex(0, 0)],
            [Complex(0, 0), Complex(2, 2), Complex(0, 0)],
        ])
        print(linear_combination([cm1, cm2], [Complex(10, 0), Complex(-2, 1)]))
        cm1 = Matrix([
            [complex(1, 1), complex(0, 0), complex(0, 0)],
            [complex(0, 0), complex(1, -1), complex(0, 0)],
        ])
        cm2 = Matrix([
            [complex(0, -1), complex(0, 0), complex(0, 0)],
            [complex(0, 0), complex(2, 2), complex(0, 0)],
        ])
        print(linear_combination([cm1, cm2], [complex(10, 0), complex(-2, 1)]))
        print(f"{'-' * 50}")
        cm3 = Matrix([
            [1, Complex(0, 1)],
            [Complex(2, -1), 4.5],
        ])
        cm4 = Matrix([
            [Complex(1, 1), 0],
            [2, Complex(3, -3)],
        ])
        cm5 = Matrix([
            [1, 0 + 1j],
            [2 - 1j, 4.5],
        ])
        cm6 = Matrix([
            [1 + 1j, 0],
            [2, 3 - 3j],
        ])
        print(linear_combination([cm3, cm4], [-1, 1]))
        print(linear_combination([cm5, cm6], [-1, 1]))
        

        # Invalid Tests
        print("\n=== Error tests ===")
        try:
            print(linear_combination([Vector([])], []))
        except Exception as err:
            print(err)
        try:
            print(linear_combination([Matrix([])], [1]))
        except Exception as err:
            print(err)
        try:
            print(linear_combination([Vector([1])], [1, 2]))
        except Exception as err:
            print(err)

    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"Error exception {err} \nline: {err.__traceback__.tb_lineno}")


if __name__ == "__main__":
    main()
