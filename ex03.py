from src.vector import Vector
from src.matrice import Matrix


def main():
    try:
        # Frobenius Dot scalar
        # Vector tests
        u = Vector([0., 0.])
        v = Vector([1., 1.])
        print(u.dot(v))

        u = Vector([1., 1.])
        v = Vector([1., 1.])
        print(u.dot(v))

        u = Vector([-1., 6.])
        v = Vector([3., 2.])
        print(u.dot(v))
        
        u = Vector([-1 + 1j, 6. + 8j])
        v = Vector([3., 2.])
        print(u.dot(v))

        # Matrix tests
        u = Matrix([[4, 2], [0, 3]])
        v = Matrix([[4, 0], [1, 4]])
        print(u.dot(v))
        
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
