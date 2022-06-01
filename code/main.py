import copy

from utils import check_add_tile


def generate_poly_ominoes(n):
    """ Generates all free poly_ominoes of order i, where i <= n
    """
    curr_poly_ominoes = [[[0, 0]]]
    for _ in range(n):
        current_poly_ominoes = copy.deepcopy(curr_poly_ominoes)
        curr_poly_ominoes = []

        for curr_poly_omino in current_poly_ominoes:
            for tile in curr_poly_omino:
                # Add a tile left of current tile
                check_add_tile([tile[0] - 1, tile[1]], curr_poly_omino, curr_poly_ominoes)

                # Add a tile left of current tile
                check_add_tile([tile[0], tile[1] - 1], curr_poly_omino, curr_poly_ominoes)

                # Add a tile left of current tile
                check_add_tile([tile[0] + 1, tile[1]], curr_poly_omino, curr_poly_ominoes)

                # Add a tile left of current tile
                check_add_tile([tile[0], tile[1] + 1], curr_poly_omino, curr_poly_ominoes)

        yield current_poly_ominoes


def print_poly_ominoes(poly_omino_list):
    """ Prints a tiled matrix for each poly-omanoe of order n
    """
    for poly_omino in poly_omino_list:
        n = len(poly_omino)
        matrix = [[' ' for _ in range(n)] for _ in range(n)]
        for tile in poly_omino:
            matrix[tile[0]][tile[1]] = 'x'

        print(*matrix, sep='\n')
        print('\n')


if __name__ == '__main__':
    poly_omino_order = int(input('Input order of poly-omino: '))
    check_print_poly_ominoes = input('Print poly-ominoes (y/N)? ')

    poly_ominoe_generator = generate_poly_ominoes(poly_omino_order)

    for i in range(poly_omino_order):
        order_i_poly_ominoes = next(poly_ominoe_generator)
    
    if check_print_poly_ominoes in ['y', 'Y']:
        print_poly_ominoes(order_i_poly_ominoes)

    print(f'There are {len(order_i_poly_ominoes)} order {poly_omino_order} poly-ominoes')
