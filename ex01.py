from src.vector import Vector, _is_number
from src.matrice import Matrix
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

        # Matrix tests
        print("\n=== Matrix tests ===")
        m1 = Matrix([[1., 0., 0.], [0., 1., 0.]])
        m2 = Matrix([[1., 0., 0.], [0., 1., 0.]])
        print(linear_combination([m1, m2], [10., -2.]))

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
