# Matrix2x2 Operations

This Python project implements a `Matrix2x2` class that represents a 2x2 matrix and supports basic matrix operations such as addition, subtraction, multiplication, and determinant calculation.

## Features

- **Addition**: Add two 2x2 matrices.
- **Subtraction**: Subtract one 2x2 matrix from another.
- **Multiplication**: Multiply two 2x2 matrices.
- **Determinant**: Calculate the determinant of a 2x2 matrix.

## Class Methods

### `__init__(self, a, b, c, d)`
Initializes a 2x2 matrix with elements:
| a, b |
| c, d |

### `__add__(self, other)`
Adds two matrices element-wise.

### `__sub__(self, other)`
Subtracts one matrix from another element-wise.

### `__mul__(self, other)`
Multiplies two matrices using matrix multiplication rules.

### `determinant(self)`
Calculates the determinant of the matrix.

### `__str__(self)`
Returns a string representation of the matrix in a readable format.

## Usage

To use the `Matrix2x2` class, you can instantiate it with four integer values and perform operations as shown below:

```python
# Example usage
from matrix2x2 import Matrix2x2

# Creating two matrices
m1 = Matrix2x2(1, 2, 3, 4)
m2 = Matrix2x2(5, 6, 7, 8)

print("Matrix 1:")
print(m1)

print("Matrix 2:")
print(m2)

# Addition
print("Addition of m1 and m2:")
print(m1 + m2)

# Subtraction
print("Subtraction of m1 from m2:")
print(m1 - m2)

# Multiplication
print("Multiplication of m1 and m2:")
print(m1 * m2)

# Determinant
print("Determinant of m1:", m1.determinant())
print("Determinant of m2:", m2.determinant())
