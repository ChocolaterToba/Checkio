def checkio(matrix):
    if (matrix[0][0] * a + matrix[1][0] * b + matrix[2][0] * c % 360 == 0 and
        matrix[0][1] * a + matrix[1][1] * b + matrix[2][1] * c % 360 == 225 and
        matrix[0][2] * a + matrix[1][2] * b + matrix[2][2] * c % 360 == 315
        for a in range(181) for b in range(181) for c in range(181)):
        return [a, b, c]