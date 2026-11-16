# The Matrix — Linear Algebra



## Mathematical notation

- A **scalar** is a single number, usually written \(\lambda\) or \(a\).
- A **vector** is an ordered list of numbers, e.g. \(u=(u_1,\ldots,u_n)\in\mathbb{R}^n\).
- A **matrix** is a rectangular array of numbers. \(A\in\mathbb{R}^{m\times n}\) has \(m\) rows and \(n\) columns.
- \(A_{ij}\) means the element in row \(i\), column \(j\).
- \(\sum\) means “sum over”; \(|x|\) is absolute value; \(\sqrt{x}\) is the square root.
- Unless otherwise stated, the subject asks for real-valued calculations (`f32` in its Rust prototypes).

---

## Ex00 — Add, subtract and scale

**Goal:** Implement addition and subtraction of vectors/matrices with matching dimensions, and multiplication by a scalar.

### Vector operations

For \(u,v\in\mathbb{R}^n\) and scalar \(\lambda\in\mathbb{R}\):

\[
u+v=(u_1+v_1,\ldots,u_n+v_n)
\]
\[
u-v=(u_1-v_1,\ldots,u_n-v_n)
\]
\[
\lambda u=(\lambda u_1,\ldots,\lambda u_n)
\]

**Example:** If \(u=(2,3)\), \(v=(5,7)\), and \(\lambda=2\):

- \(u+v=(7,10)\)
- \(u-v=(-3,-4)\)
- \(2u=(4,6)\)

### Matrix operations

For matrices of the same shape, apply the operation to corresponding entries:

\[
(A+B)_{ij}=A_{ij}+B_{ij},\qquad (A-B)_{ij}=A_{ij}-B_{ij},\qquad (\lambda A)_{ij}=\lambda A_{ij}.
\]

**Important:** Addition and subtraction require equal dimensions (same vector length or same matrix rows and columns). Scaling does not change the shape.


---

## Ex01 — Linear combination

**Goal:** Combine several vectors after multiplying each one by its corresponding scalar coefficient.

Given vectors \(u_1,\ldots,u_k\in\mathbb{R}^n\) and coefficients \(\lambda_1,\ldots,\lambda_k\in\mathbb{R}\):

\[
w=\sum_{i=1}^{k}\lambda_i u_i
=\lambda_1u_1+\lambda_2u_2+\cdots+\lambda_ku_k.
\]

Coordinate by coordinate:

\[
w_j=\sum_{i=1}^{k}\lambda_i(u_i)_j,\qquad j=1,\ldots,n.
\]

**Example:** Let \(u_1=(1,0)\), \(u_2=(0,1)\), with coefficients \(3\) and \(-2\):

\[
w=3(1,0)-2(0,1)=(3,-2).
\]

**What to understand:** A linear combination is a sum of scaled vectors. The result belongs to the same vector space. The number of vectors must match the number of coefficients, and the vectors must have compatible dimensions.

---

## Ex02 — Linear interpolation (LERP)

**Goal:** Find a point between two values/vectors/matrices according to a parameter \(t\).

For two objects \(u,v\) of the same vector-space type:

\[
\operatorname{lerp}(u,v,t)=(1-t)u+tv.
\]

The subject specifies \(t\in[0,1]\):

- \(t=0\): result is \(u\).
- \(t=1\): result is \(v\).
- \(t=0.5\): result is the midpoint.

**Example:** Let \(u=2\), \(v=10\), and \(t=0.25\):

\[
(1-0.25)\cdot2+0.25\cdot10=1.5+2.5=4.
\]

For vectors, the same formula is applied to the whole vector:

\[
\operatorname{lerp}((2,1),(4,3),0.5)=(3,2).
\]

**What to understand:** Interpolation is a weighted combination of two endpoints. With \(t\) between 0 and 1, the result lies on the segment joining them. The formula also works outside this interval to extend along the same line, although the required subject interval is \([0,1]\).

---

## Ex03 — Dot product

**Goal:** Compute a scalar from two vectors of the same dimension.

For \(u,v\in\mathbb{R}^n\):

\[
u\cdot v=\langle u,v\rangle=\sum_{i=1}^{n}u_iv_i.
\]

**Example:** If \(u=(-1,6)\) and \(v=(3,2)\):

\[
u\cdot v=(-1)\cdot3+6\cdot2=-3+12=9.
\]

**Geometric meaning:**

\[
u\cdot v=\|u\|\,\|v\|\cos(\theta),
\]

where \(\theta\) is the angle between the vectors. Therefore:

- Positive dot product: angle is acute (for nonzero vectors).
- Zero dot product: vectors are orthogonal (perpendicular).
- Negative dot product: angle is obtuse.

**What to understand:** The dot product measures how much two vectors point in the same direction. It is also the central operation used to calculate matrix multiplication.


---

## Ex04 — Norm

**Goal:** Measure the length/magnitude of a vector. The subject asks for three norms.

For \(v=(v_1,\ldots,v_n)\):

### 1-norm (Manhattan / Taxicab norm)

\[
\|v\|_1=\sum_{i=1}^{n}|v_i|.
\]

It adds the absolute values of all coordinates.

### 2-norm (Euclidean norm)

\[
\|v\|_2=\|v\|=\sqrt{\sum_{i=1}^{n}v_i^2}.
\]

This is the usual straight-line length of a vector.

### Infinity norm (supremum norm)

\[
\|v\|_\infty=\max_{1\leq i\leq n}|v_i|.
\]

It takes the largest absolute coordinate.

**Example:** For \(v=(-1,-2)\):

\[
\|v\|_1=|-1|+|-2|=3,
\]
\[
\|v\|_2=\sqrt{(-1)^2+(-2)^2}=\sqrt5\approx2.236,
\]
\[
\|v\|_\infty=\max(1,2)=2.
\]

**What to understand:** A norm is a measure of size/length. The three norms measure it in different ways. Norm results are real and non-negative; the zero vector has norm zero.

---

## Ex05 — Cosine of the angle between two vectors

**Goal:** Compute the cosine of the angle between two nonzero vectors of equal dimension, without calling a standard-library cosine function.

Start with the dot-product identity:

\[
u\cdot v=\|u\|\,\|v\|\cos(\theta).
\]

Rearrange it:

\[
\boxed{\cos(\theta)=\frac{u\cdot v}{\|u\|\,\|v\|}}
\]

**Example:** Let \(u=(1,0)\), \(v=(0,1)\):

\[
u\cdot v=0,\quad \|u\|=1,\quad\|v\|=1,
\]
\[
\cos(\theta)=\frac{0}{1\cdot1}=0.
\]

The vectors are perpendicular, so their angle is 90 degrees.

**Interpretation:**

- \(1\): same direction.
- \(0\): perpendicular.
- \(-1\): opposite directions.

The formula is undefined if either vector is zero because its norm would make the denominator zero. It is also undefined for vectors of different dimensions according to the subject.

**Connection to data science:** The subject relates this geometric cosine to the Pearson correlation coefficient: both describe alignment, although Pearson correlation uses centered statistical data.


---

## Ex06 — Cross product

**Goal:** Compute the cross product of two 3-dimensional real vectors.

For \(u=(u_1,u_2,u_3)\) and \(v=(v_1,v_2,v_3)\):

\[
u\times v=
\begin{pmatrix}
u_2v_3-u_3v_2\\
u_3v_1-u_1v_3\\
u_1v_2-u_2v_1
\end{pmatrix}.
\]

**Example:** Let \(u=(1,2,3)\), \(v=(4,5,6)\):

\[
u\times v=
\begin{pmatrix}
2\cdot6-3\cdot5\\
3\cdot4-1\cdot6\\
1\cdot5-2\cdot4
\end{pmatrix}
=
\begin{pmatrix}-3\\6\\-3\end{pmatrix}.
\]

**Geometric meaning:** The result is perpendicular to both input vectors. Its magnitude is the area of the parallelogram formed by the two vectors:

\[
\|u\times v\|=\|u\|\,\|v\|\sin(\theta).
\]

The direction follows the right-hand rule. If the vectors are parallel, the cross product is the zero vector.

**Important:** This exercise is specifically for 3D vectors. Unlike the dot product, the ordinary cross product does not produce a 3D vector in arbitrary dimensions.

---

## Ex07 — Linear map and matrix multiplication

**Goal:** Implement matrix-vector multiplication and matrix-matrix multiplication.

### Matrix multiplied by a vector

Let \(A\in\mathbb{R}^{m\times n}\) and \(u\in\mathbb{R}^{n}\). The result is a vector in \(\mathbb{R}^{m}\):

\[
(Au)_i=\sum_{j=1}^{n}A_{ij}u_j.
\]

**Example:**

\[
A=\begin{pmatrix}2&0\\0&2\end{pmatrix},\quad
u=\begin{pmatrix}4\\2\end{pmatrix}
\quad\Longrightarrow\quad
Au=\begin{pmatrix}8\\4\end{pmatrix}.
\]

Each output coordinate is the dot product of one row of \(A\) with the input vector.

### Matrix multiplied by a matrix

Let \(A\in\mathbb{R}^{m\times n}\) and \(B\in\mathbb{R}^{n\times p}\). The result is \(C=AB\in\mathbb{R}^{m\times p}\):

\[
C_{ij}=\sum_{k=1}^{n}A_{ik}B_{kj}.
\]

Each output entry is the dot product of a row of \(A\) and a column of \(B\).

**Dimension rule:** The number of columns of the left matrix must equal the number of rows of the right matrix. In \((m\times n)(n\times p)\), the result has shape \(m\times p\).

**Linear-map meaning:** A matrix represents a linear transformation. It transforms an input vector into an output vector. Matrix multiplication represents composition of linear transformations; order matters, and in general \(AB\neq BA\).

---

## Ex08 — Trace

**Goal:** Compute the trace of a square matrix: the sum of its main-diagonal entries.

For \(A\in\mathbb{R}^{n\times n}\):

\[
\operatorname{Tr}(A)=\sum_{i=1}^{n}A_{ii}.
\]

**Example:**

\[
A=\begin{pmatrix}2&-5&0\\4&3&7\\-2&3&4\end{pmatrix}
\quad\Longrightarrow\quad
\operatorname{Tr}(A)=2+3+4=9.
\]

**What to understand:** Only the main diagonal is used. The matrix must be square. The trace is a scalar, not another matrix.

---

## Ex09 — Transpose

**Goal:** Exchange the rows and columns of a matrix.

For \(A\in\mathbb{R}^{m\times n}\), its transpose \(A^T\) belongs to \(\mathbb{R}^{n\times m}\):

\[
(A^T)_{ij}=A_{ji}.
\]

**Example:**

\[
A=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}
\quad\Longrightarrow\quad
A^T=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}.
\]

The first row becomes the first column, the second row becomes the second column, and so on.

**What to understand:** Transposition changes the shape from \(m\times n\) to \(n\times m\), but does not change the values themselves. For complex matrices, the related operation is the conjugate transpose: transpose and take the complex conjugate of each entry. The required exercise uses real numbers.

---

## Ex10 — Row-echelon form (REF)

**Goal:** Transform a matrix into row-echelon form using elementary row operations.

A matrix is in row-echelon form when:

1. Any rows containing only zeros are at the bottom.
2. The first nonzero entry (the **pivot**) of each nonzero row is to the right of the pivot in the row above it.
3. All entries below each pivot are zero.

The subject does not require pivots to equal 1, nor does it require zeros above pivots. Those are features associated with reduced row-echelon form (RREF), a different, more restrictive form.

### Main row operation

To eliminate an entry below a pivot, use:

\[
L_i\leftarrow L_i-\frac{a_{ik}}{a_{kk}}L_k,
\]

where \(a_{kk}\) is the pivot and \(a_{ik}\) is the entry to eliminate. This operation makes the entry in row \(i\), pivot column \(k\), equal to zero.

If the current pivot is zero, look for a suitable nonzero entry below it and swap rows. If no such entry exists, move to another column to find the next pivot.

**Example:**

\[
A=\begin{pmatrix}1&2\\3&4\end{pmatrix}.
\]

Use \(L_2\leftarrow L_2-3L_1\):

\[
\begin{pmatrix}1&2\\3&4\end{pmatrix}
\longrightarrow
\begin{pmatrix}1&2\\0&-2\end{pmatrix}.
\]

This is row-echelon form. Dividing the second row by \(-2\) would make its pivot 1, but that extra normalization is not necessary for REF.

**Why it matters:** REF exposes the pivot positions and helps solve linear systems, determine rank, and identify dependent rows. Floating-point implementations need a tolerance when deciding whether a value is effectively zero.

---

## Ex11 — Determinant

**Goal:** Compute the determinant of a square matrix. The subject requires dimensions up to \(4\times4\).

The determinant is a scalar associated with a square matrix. It describes the signed volume-scaling factor of the linear transformation represented by the matrix.

### 1×1

\[
\det([a])=a.
\]

### 2×2

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
\det(A)=ad-bc.
\]

**Example:**

\[
\det\begin{pmatrix}1&2\\3&4\end{pmatrix}=1\cdot4-2\cdot3=-2.
\]

### 3×3 (cofactor expansion along the first row)

\[
\det\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix}
=a(ei-fh)-b(di-fg)+c(dh-eg).
\]

### 4×4 and larger

One general method is **cofactor expansion**: expand along a row or column using signed minors. For a chosen row \(i\):

\[
\det(A)=\sum_{j=1}^{n}(-1)^{i+j}A_{ij}\det(M_{ij}),
\]

where \(M_{ij}\) is the matrix obtained by deleting row \(i\) and column \(j\). For a 4×4 matrix, this reduces the calculation to four 3×3 determinants.

### Geometric meaning and singularity

- \(|\det(A)|\) is the factor by which the transformation scales area (in 2D), volume (in 3D), or the corresponding higher-dimensional volume.
- A negative determinant means the transformation also reverses orientation.
- If \(\det(A)=0\), the transformation collapses at least one dimension; the matrix is singular and has no inverse.
- If \(\det(A)\neq0\), the square matrix is invertible.

**Important for evaluation:** Be able to explain what determinant zero means and why the absolute value represents volume scaling.


---

## Ex12 — Inverse matrix

**Goal:** Compute the inverse of a square matrix when it exists. The inverse reverses the transformation represented by the original matrix.

For a square matrix \(A\), its inverse \(A^{-1}\) satisfies:

\[
A^{-1}A=AA^{-1}=I_n,
\]

where \(I_n\) is the identity matrix (ones on the main diagonal and zeros elsewhere).

### 2×2 formula

For

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

if \(ad-bc\neq0\), then

\[
A^{-1}=\frac{1}{ad-bc}
\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.
\]

**Example:**

\[
A=\begin{pmatrix}2&0\\0&2\end{pmatrix},\qquad
A^{-1}=\begin{pmatrix}1/2&0\\0&1/2\end{pmatrix}.
\]

Check:

\[
AA^{-1}=\begin{pmatrix}2&0\\0&2\end{pmatrix}
\begin{pmatrix}1/2&0\\0&1/2\end{pmatrix}
=I_2.
\]

### Gauss–Jordan method

A general practical method is to build the augmented matrix \([A\mid I]\), then use elementary row operations to turn the left side into the identity:

\[
[A\mid I]\ \longrightarrow\ [I\mid A^{-1}].
\]

If a pivot cannot be found for a column, the matrix is singular and the function should return an error. In floating-point code, use a tolerance to detect pivots close to zero.

**What to understand:** An inverse exists exactly for nonsingular square matrices. It undoes the effect of the original matrix. Matrix multiplication is not commutative, so the inverse identities are stated on both sides.


---

## Ex13 — Rank

**Goal:** Compute the rank of a matrix.

The **rank** is the number of linearly independent rows or columns. Equivalently, it is the number of pivots (nonzero rows) in a row-echelon form of the matrix.

\[
\operatorname{rank}(A)=\text{number of pivots in REF}(A).
\]

**Example:**

\[
A=\begin{pmatrix}
1&2&0&0\\
2&4&0&0\\
-1&2&1&1
\end{pmatrix}.
\]

The second row is twice the first, so it does not add a new independent row. The first and third rows are independent. Therefore:

\[
\operatorname{rank}(A)=2.
\]

**Geometric meaning:** The rank is the dimension of the image (also called the column space) of the linear transformation. It tells you how many independent directions remain reachable after applying the matrix.

- Full row rank means all rows are independent.
- Full column rank means all columns are independent.
- For a square \(n\times n\) matrix, rank \(n\) means it is invertible; rank less than \(n\) means it is singular.

**Connection with REF:** Compute row-echelon form, then count its nonzero rows/pivots. Do not count rows that contain only zeros.


---

## How the exercises build on one another

| Exercise | Main concept | Useful prerequisite / reuse |
|---|---|---|
| Ex00 | Vector and matrix arithmetic | Coordinate-wise operations |
| Ex01 | Linear combination | Ex00 scaling and addition |
| Ex02 | Linear interpolation | Ex00 and linear combination |
| Ex03 | Dot product | Multiplication and summation |
| Ex04 | Vector norms | Absolute value, squares, sum, maximum |
| Ex05 | Cosine similarity | Ex03 dot product + Ex04 Euclidean norm |
| Ex06 | Cross product | 3D vector coordinates |
| Ex07 | Linear maps and matrix multiplication | Dot product, row/column operations |
| Ex08 | Trace | Matrix diagonal |
| Ex09 | Transpose | Matrix indexing and dimensions |
| Ex10 | Row-echelon form | Row swaps and row operations |
| Ex11 | Determinant | Square matrices, minors/cofactors or elimination |
| Ex12 | Inverse | Identity matrix, pivots, row operations, singularity |
| Ex13 | Rank | Row-echelon form and pivots |

