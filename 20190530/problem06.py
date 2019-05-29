def get_heaviest_neighbour_cell(drawn_array):
    """
    find the cell whose total sum of it’s neighbour weight is maximum
    :param drawn_array: array: information of the table
    :return: tuple (0:the row and 1:column of the cell)
    """
    heaviest_cell_coordinate = (0, 0)
    i_num = len(drawn_array)
    j_num = len(drawn_array[0])
    heaviest_cell_weight = 0
    for i in range(i_num):
        for j in range(j_num):
            total_wight = 0
            if (i - 1) >= 0:
                total_wight += drawn_array[i - 1][j]
            if (i + 1) < i_num:
                total_wight += drawn_array[i + 1][j]
            if (j - 1) >= 0:
                total_wight += drawn_array[i][j - 1]
            if (j + 1) < j_num:
                total_wight += drawn_array[i][j - 1]

            if heaviest_cell_weight < total_wight:
                heaviest_cell_coordinate = (i, j)
                heaviest_cell_weight = total_wight
    return heaviest_cell_coordinate


def get_drawn_table(drawn_table_info):
    """
    return table's information
    :param drawn_table_info: tuple: table's meta data
    :return: array: table's information
    """
    i_num = drawn_table_info[0]
    j_num = drawn_table_info[1]
    blanked_cells = drawn_table_info[2]

    new_array = []
    for i in range(i_num):
        new_array.append([])
        for j in range(j_num):
            if blanked_cells.count([i, j]) >= 1:
                new_array[i].append(0)
            else:
                new_array[i].append((i + j) * 3 - 10)
    return new_array


def print_drawn_table(drawn_table):
    """
    print the table
    :param drawn_table: table's meta data
    :return: void
    """
    for i in range(len(drawn_table)):
        for j in range(len(drawn_table[i])):
            print("%3.0f" % drawn_table[i][j], end="")
        print()
    print()


def picture_drawn_table(drawn_table):
    """
    picture the table
    :param drawn_table: table information
    :return: void
    """
    for i in range(len(drawn_table)):
        for j in range(len(drawn_table[i])):
            if drawn_table[i][j] == 0:
                print('  ', end="")
            else:
                print('▓▓', end="")
            print(' ', end="")
        print()
    print()


def get_drawn_table_info():
    """
    define the table information
    :return: tuple(row, column, blanked cell's coordinates)
    """
    row_num = 8
    column_num = 10
    blanked_cells = [
        [0, 0]
        , [0, 7]
        , [0, 8]
        , [1, 2]
        , [2, 1]
        , [2, 2]
        , [2, 3]
        , [2, 4]
        , [2, 5]
        , [3, 5]
        , [3, 8]
        , [4, 5]
        , [4, 8]
        , [5, 1]
        , [5, 2]
        , [5, 3]
        , [5, 4]
        , [5, 5]
        , [5, 8]
        , [6, 5]
        , [7, 3]
        , [7, 4]
        , [7, 5]
        , [7, 6]
    ]
    return row_num, column_num, blanked_cells


def main():
    # define 2D array
    drawn_table = get_drawn_table(get_drawn_table_info())
    picture_drawn_table(drawn_table)
    print_drawn_table(drawn_table)

    # receive (6, 7)
    heaviest_cell_coordinate = get_heaviest_neighbour_cell(drawn_table)
    print('The cell whose total sum of it’s neighbour weight is maximum is', heaviest_cell_coordinate)


main()
