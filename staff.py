def print_array(matrix, msg="", sep='\n'):
    n = matrix.shape[0]
    m = None

    if msg != "":
        print(msg)
    if len(matrix.shape) == 2:
        m = matrix.shape[1]

    if len(matrix.shape) == 2:
        for i in range(n):
            for j in range(m):
                print('{:>8.5f}'.format(matrix[i, j]), end='')
            print(sep, end='')

    elif len(matrix.shape) == 1:
        for i in range(n):
            print('{:>8.5f}'.format(matrix[i]), end='')
        print(sep, end='')


def separator(times=2, dig='-', count=30):
    for i in range(times):
        print(str(dig) * count)
