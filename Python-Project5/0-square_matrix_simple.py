def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        squared_row = []
        for value in row:
            squared_row.append(value ** 2)
        new_matrix.append(squared_row)

    return new_matrix
