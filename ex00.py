from src.vector import Vector
from src.matrice import Matrix
from src.complex import Complex


def main():
    try:
        # Vector tests
        print("=== Vector tests ===")

        u1 = Vector([2, 3])
        u2 = Vector([2, 3])
        v = Vector([7, 7])

        print("Initial u:")
        print(u1)

        print("After addition:")
        u1.add(v)
        print(u1)
        u2 = u2 + v
        print('----')
        print(u2)

        print("After subtraction:")
        u1.sub(v)
        print(u1)
        print('----')
        u2 = u2 - v
        print(u2)
        
        u1 = Vector([4, 3])
        u2 = Vector([4, 3])
        print("After scalar multiplication:")
        u1.scl(5)
        print(u1)
        print('----')
        print(u2 * 5)

        print("=== Test of complex number ===")
        u1 = Vector([Complex(2, 1), 3])
        u2 = Vector([Complex(2, 1), 3])
        u3 = Vector([complex(2, 1), 3])
        u4 = Vector([complex(2, 1), 3])
        
        u1.add(u2)
        print(u1)
        print('---')
        print(u3.add(u4))
        print("===")
        
        u1.sub(u2)
        print(u1)
        print('---')
        print(u3.sub(u4))
        print("===")
        
        u1.scl(5)
        print(u1)
        print('---')
        print(u3.scl(5))
        print("===")
        
        u2.scl(Complex(2, 5))
        print(u2)
        print('---')
        print(u4.scl(complex(2, 5)))

        # Matrix tests
        print("\n=== Matrix tests ===")

        u1 = Matrix([[1., 2.], [3., 4.]])
        u2 = Matrix([[1., 2.], [3., 4.]])
        v = Matrix([[7., 4.], [-2., 2.]])

        print("Initial matrix:")
        print(u1)

        u1.add(v)
        print("After addition:")
        print(u1)
        u2 = u2 + v
        print(u2)

        u1.sub(v)
        print("After subtraction:")
        print(u1)
        u2 = u2 - v
        print(u2)

        u1.scl(2)
        print("After scalar multiplication:")
        print(u1)
        print(u2 * 2)
        
        print("=== Test of complex number ===")

        u1 = Matrix([[Complex(1, 2), Complex(3, -1)],
                    [Complex(0, 4), Complex(5, 0)]])

        u2 = Matrix([[complex(1, 2), complex(3, -1)],
                    [complex(0, 4), complex(5, 0)]])

        v1 = Matrix([[Complex(7, -1), Complex(4, 3)],
                    [Complex(-2, 1), Complex(2, -2)]])
        v2 = Matrix([[complex(7, -1), complex(4, 3)],
                    [complex(-2, 1), complex(2, -2)]])

        print("Initial matrix:")
        print(u1)
        print("===")

        u1.add(v1)
        print("After addition:")
        print(u1)
        u2 = u2 + v2
        print(u2)
        print("===")

        u1.sub(v1)
        print("After subtraction:")
        print(u1)
        u2 = u2 - v2
        print(u2)
        print("===")

       
        scalar = Complex(2, -1)
        scalar1 = complex(2, -1)
        u1.scl(scalar)
        print("After scalar multiplication:")
        print(u1)
        print(u2 * scalar1)
        print("===")

        # Invalid Tests
        print("\n=== Error tests ===")

        try:
            Vector([])
        except (ValueError, AssertionError) as err:
            print(f"Expected vector error: {err}")

        try:
            Vector([1, 2]).add(Vector([1, 2, 3]))
        except (ValueError, AssertionError) as err:
            print(f"Expected vector error: {err}")

        try:
            Matrix([[1, 2]]).add(Matrix([[1, 2], [3, 4]]))
        except (ValueError, AssertionError) as err:
            print(f"Expected matrix error: {err}")

    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
