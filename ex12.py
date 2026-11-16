from src.matrice import Matrix
from src.complex import Complex

def identity(n):
    return Matrix([[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)])

def test_inverse():
    print("\n=== inverse tests ===")

    u = Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
    print(u.inverse())
    print('--------------')
    # [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

 
    u = Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]])
    print(u.inverse())
    print('--------------')
    # [[0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]]


    u = Matrix([[1., 2.], [3., 4.]])
    print(u.inverse())
    print('--------------')

    u = Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
    print(u.inverse())
    print('--------------')
    # [[0.649425287, 0.097701149, -0.655172414],
    #  [-0.781609195, -0.126436782, 0.965517241],
    #  [0.143678161, 0.074712644, -0.206896552]]


    u = Matrix([[1., 2.], [2., 4.]])
    try:
        print(u.inverse())
    except ValueError as e:
        print("Erreur :", e)

def test_inverse_complex():
    print("\n=== inverse tests Complex ===")


    u = Matrix([[Complex(4, 4), Complex(3, 3)], [Complex(2, 2), Complex(1, 1)]])
    print(u.inverse())
    print('--------------')

    u = Matrix([[complex(4, 4), complex(3, 3)], [complex(2, 2), complex(1, 1)]])
    print(u.inverse())



def main():
    try:
        test_inverse()
        test_inverse_complex()
    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
