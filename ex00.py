from src.vector import Vector
from src.matrice import Matrix


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
        print(u2 + v)

        print("After subtraction:")
        u1.sub(v)
        print(u1)
        print(u2 - v)

        u1 = Vector([2 + 1j, 3])
        u2 = Vector([2 + 1j, 3])
        print("After scalar multiplication:")
        u1.scl(2 + 5j)
        print(u1)
        print(u2 * (2 + 5j))

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
        print(u2 + v)

        u1.sub(v)
        print("After subtraction:")
        print(u1)
        print(u2 - v)

        u1.scl(2)
        print("After scalar multiplication:")
        print(u1)
        print(u2 * 2)

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
