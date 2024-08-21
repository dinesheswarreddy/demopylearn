class Matrix2x2:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        return Matrix2x2(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __sub__(self, other):
        return Matrix2x2(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)

    def __mul__(self, other):
        a = self.a * other.a + self.b * other.c
        b = self.a * other.b + self.b * other.d
        c = self.c * other.a + self.d * other.c
        d = self.c * other.b + self.d * other.d
        return Matrix2x2(a, b, c, d)

    def determinant(self):
        return self.a * self.d - self.b * self.c

    def __str__(self):
        return f'''                  
                   |{self.a}, {self.b}|
                   |{self.c}, {self.d}|
                 ''' 

a, b, c, d = map(int, input("4 values sep by spaces for M-1: ").split())
e,f,g,h = map(int, input("4 values sep by spaces for M-2: ").split())
m1 = Matrix2x2(a, b, c, d)
m2 = Matrix2x2(e, f, g, h)

print("Matrix-1:",m1)
print("Matrix-2:",m2)

# Addition
print("m1 + m2 =", m1 + m2)

# Subtraction
print("m1 - m2 =", m1 - m2)

# Multiplication
print("m1 * m2 =", m1 * m2)

# Determinant
print("Determinant of m1 =", m1.determinant())
print("Determinant of m2 =", m2.determinant())

#type
print("\n Type :- ")
print(type(m1))
