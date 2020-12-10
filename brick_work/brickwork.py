from collections import Counter, deque


def take_inputs_for_wall():
    first_row = []
    n, m = input("Please enter the size  of the wall on single line, separated by space (N M):\n").split()
    # We take input from the console for N and M.

    n, m = test_n_and_m_are_valid(n, m)
    # This test is to validates that n, m are :
    # - integers,
    # - less then 100,
    # - positive numbers,
    # - even numbers
    # and rise error if not.

    print("Please enter the first layer of bricks.\n" +
          "Add a single value separated by a space for each line N and the following column M")
    for x in range(n):
        first_row.append(input().split())
    # We take input from the console for the 1st layer of bricks and save it as 2d matrix:

    test_if_input_matrix_is_valid(n, m, first_row)
    # This test validate the matrix :
    # - check if the dimensions are respond to N and M
    # - having pairs(2) of unique numbers
    # - check if the pairs are next to each other
    # and rise error if not.

    return n, m, first_row
    # If all checks pass we return the input


def test_n_and_m_are_valid(n, m):
    try:
        n, m = int(n), int(m)
    except ValueError:
        raise Exception("N and M must be integers.")
        # we test if N and M are integers

    if n > 100 or m > 100:
        raise Exception("N and M must be a less then 100.")
        # we test if N and M are less then 100

    if n <= 0 or m <= 0:
        raise Exception("N and M must be a positive numbers.")
        # We test if N and M are negative numbers

    if n % 2 != 0 or m % 2 != 0:
        raise Exception("N and M must be a even numbers.")
        # We test if N and M are even numbers

    return n, m
    # If we pass all test we return N and M


def test_if_matrix_have_right_number_of_elements_and_returns_them(matrix):
    temp_list_to_count = []
    number_of_bricks = []
    for x in matrix:
        temp_list_to_count += x
    # We are making a new temp. list from the first layer witch we can manipulate.

    temp_list_to_count = dict(Counter(temp_list_to_count))
    # We are making dict from the temp list with
    # key -> the unique numbers in the 1st layer
    # value -> the count of each unique number

    for key, val in temp_list_to_count.items():
        if val != 2:
            raise Exception("Wrong number of half-bricks")
        number_of_bricks.append(key)
    # We check if every unique number in the matrix have count of two (2)

    return number_of_bricks


def find_index_of_elements_in_matrix(element, matrix):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                res.append((i, j))
    # we are finding the indexs for a specific element(number) in the matrix

    return res


def checking_if_elements_in_matrix_are_next_to_each_other(matrix, number_of_bricks):
    for element in number_of_bricks:
        list_of_idx = find_index_of_elements_in_matrix(element, matrix)
        x1, x2, y1, y2 = list_of_idx[0][0], list_of_idx[1][0], list_of_idx[0][1], list_of_idx[1][1]
        if abs(x1 - x2) != 1 and abs(y1 - y2) != 1:
            raise Exception("Half-bricks are not next to each other.")
    # We are checking if the unique elements(numbers) are next to each other by taking the indexs of them
    # and making sure the difference between then is module of 1.


def test_if_input_matrix_is_valid(n, m, matrix):
    number_of_bricks = test_if_matrix_have_right_number_of_elements_and_returns_them(matrix)
    checking_if_elements_in_matrix_are_next_to_each_other(matrix, number_of_bricks)
    # we combine the the previous test in to one.

    if len(matrix) != n:
        raise Exception("The rows in the wall are too many or not enough.")
    for row in matrix:
        if len(row) != m:
            raise Exception("The cows in the wall are too many or not enough.")
    # We add a simple test to see if the dimensions are according to the input of N and M


def solution():
    n, m, matrix = take_inputs_for_wall()
    if n > 2:
        return format_result(matrix)
    # We are assuming that the 1st layer of bricks have only unique bricks.
    # Therefore for 1st layer bigger then 4 lines
    # The top side of if will be aways different from the bottom side.

    else:
        result = []
        top_layer = matrix[0]
        new_bottom_layer = []
        second_bottom_layer = []
        for index in range(len(top_layer) - 1):
            for a in matrix:
                for b in a:
                    if b != top_layer[index] and b != top_layer[index + 1]:
                        new_bottom_layer.append(b)
        if len(new_bottom_layer) < m:
            return -1
        new_bottom_layer = new_bottom_layer[:m]
        for a in matrix:
            for b in a:
                if b not in new_bottom_layer:
                    second_bottom_layer.append(b)
        result.append(second_bottom_layer)
        result.append(new_bottom_layer)
        return format_result(result)

    # This solution rotates the 1st layer of bricks and it makes sure
    # that position of the elements don't match its top layer.
    # This solution will work ONLY if we ASSUME that the 1st layer
    # have only horizontal bricks.

    # TODO checker is the 1st layer have only horizontal bricks
    # TODO solution for when the 1st layer have vertical bricks


def format_result(matrix):
    n = len(matrix)
    m = len(matrix[0])
    n_line_to_add = []
    for index_n in range(m):
        n_line_to_add.append("*")

    for index_n in range(0, 2 * n, 3):
        matrix.insert(index_n, n_line_to_add)

    # We are adding horizontal line of stars(***) for every 3ed line.
    # If we add it on every 2nd line and we have vertical bricks the solution
    # it will brake the symmetry

    for index_n in range(len(matrix) - 1):
        for index_m in range(0, 2 * m, 3):
            matrix[index_n].insert(index_m, "*")

    # NOTE this solution won't work if we have uneven pairs of bricks made
    # by vertical ones. The solution from above those not proved that kind of answer.
    # TODO if the solution updates to provide answers with vertical bricks the format_result() have to be reworked

    for x in range(len(matrix)):
        print(" ".join(matrix[x]))


solution()
