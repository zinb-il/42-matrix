from src.matrice import Matrix
from src.functions import projection


def write_proj(matrix, path="proj"):
    t = matrix.transpose()
    with open(path, "w") as f:
        for i in range(4):
            f.write(", ".join(f"{x:.6f}" for x in t.data[i]) + "\n")

def main():
    try:
        fov = 90.0
        ratio = 1.0
        near = 0.1
        far = 100.0

        P = projection(fov, ratio, near, far)
        print(P)
        write_proj(P, "matrix_display/proj")

    except AssertionError as err:
        print(f"AssertionError: {err}")
    except Exception as err:
        print(f"Unexpected error: {type(err).__name__}: {err}")


if __name__ == "__main__":
    main()
