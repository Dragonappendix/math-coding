import matrix_math

starting_two_by_three_matrix = [
    [3, -2, 6],
    [1, 1, -8]
]

rref_two_by_three_matrix = [
    [1, 0, -2],
    [0, 1, 6]
]

def test_func():
    assert matrix_math.gauss_jordan_two_by_three(starting_two_by_three_matrix, rref_two_by_three_matrix)