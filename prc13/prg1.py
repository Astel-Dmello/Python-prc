def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

def divide_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            if matrix2[i][j] != 0:
                row.append(matrix1[i][j] / matrix2[i][j])
            else:
                row.append(float('inf'))  # Handle division by zero
        result.append(row)
    return result

def main():
    rows = int(input("Enter the number of rows for matrices: "))
    cols = int(input("Enter the number of columns for matrices: "))

    print("\nEnter elements for first matrix:")
    matrix1 = create_matrix(rows, cols)

    print("\nEnter elements for second matrix:")
    matrix2 = create_matrix(rows, cols)

    print("\nMatrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nAddition of matrices:")
    print(add_matrices(matrix1, matrix2))

    print("\nSubtraction of matrices:")
    print(subtract_matrices(matrix1, matrix2))

    print("\nMultiplication of matrices:")
    print(multiply_matrices(matrix1, matrix2))

    print("\nDivision of matrices:")
    print(divide_matrices(matrix1, matrix2))

if __name__ == "__main__":
    main()
