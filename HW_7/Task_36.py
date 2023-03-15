# def print_operation_table(operation, num_rows=6, num_columns=6):
#     print("   ", end="")
#     for j in range(1, num_columns+1):
#         print("{:>3}".format(j), end="")
#     print()
#     print("  +", end="")
#     for j in range(1, num_columns+1):
#         print("----", end="")
#     print()
#
#     for i in range(1, num_rows+1):
#         print("{:>2} |".format(i), end="")
#         row = [operation(i, j) for j in range(1, num_columns+1)]
#         row_str = " ".join("{:>2}".format(cell) for cell in row)
#         print(row_str)
#
# print_operation_table(lambda x, y: x * y)


def print_operation_table(operation, num_rows=6, num_columns=6):
    table = [[operation(row, col) for col in range(1, num_columns + 1)] for row in range(1, num_rows + 1)]
    max_width = len(str(table[num_rows - 1][num_columns - 1]))
    for row in table:
        for cell in row:
            print(str(cell).rjust(max_width), end=' ')
        print()


print_operation_table(lambda x, y: x * y)