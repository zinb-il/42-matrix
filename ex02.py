from src.vector import Vector, _is_number
from src.matrice import Matrix
from src.functions import lerp


def main():
    try:
        # Scalar tests
        print(lerp(0., 1., 0.))
        print(lerp(0., 1., 1.))
        print(lerp(0., 1., 0.5))
        print(lerp(21., 42., 0.3))
        
        # Vector tests
        print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3))
        print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0))
        print(lerp(Vector([2., 1.]), Vector([4., 2.]), 1))

        # Matrix tests
        print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20.,10.], [30., 40.]]), 0.5))
        
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
