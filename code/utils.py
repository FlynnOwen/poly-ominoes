import copy


def _rotate_anti_clockwise_90(poly_omino):
    """ Rotates a poly-ominoe anti-clockwise by 90 degrees around the y-axis (will be moved from the 4th quadrant to the 1st quadrant)
    """
    for tile in range(len(poly_omino)):
        temp = poly_omino[tile][0]
        poly_omino[tile][0] = poly_omino[tile][1]
        poly_omino[tile][1] = -temp

    return poly_omino


def _translate_down(poly_omino):
    """ Moves a poly-ominoe down from the 1st quadrant to the top position in the 4th quadrant
    """
    move = True
    while move:
        move = False

        for tile in poly_omino:
            if tile[1] < 0:
                move = True
                break

        if move:
            for tile in poly_omino:
                tile[1] += 1

    return poly_omino


def _translate_right_once(poly_omino):
    """ Moves a poly-ominoe down from the 1st quadrant to the top position in the 4th quadrant
    """
    for tile in poly_omino:
        tile[0] += 1

    return poly_omino


def _rotate_and_translate_360(new_poly_omino, curr_poly_ominoes):
    """Rotates a poly-ominoe 90 degrees anti-clockwise, and then translates it downwards until
       the whole poly-ominoe is in the 4th quadrant. Repeats this until either the poly-ominoe has been
       rotated a full 360 degrees, or we find any rotation of the poly-ominoe in our cache.
    """
    add_poly_omino = True
    rotations = 0

    while True:

        new_poly_omino = _translate_down(new_poly_omino)

        if sorted(new_poly_omino) in curr_poly_ominoes:
            add_poly_omino = False
            break

        if rotations == 3:
            break

        new_poly_omino = _rotate_anti_clockwise_90(new_poly_omino)
        rotations += 1

    if add_poly_omino:
        curr_poly_ominoes.append(sorted(new_poly_omino))


def check_add_tile(new_tile, curr_poly_omino, curr_poly_ominoes):
    """ Checks if the position we'd like to add a new tile isn't part of the current poly-ominoe.
        If it isn't we add the tile to the poly-ominoe and call function rotate_and_translate_360
    """
    if new_tile not in curr_poly_omino:
        new_poly_omino = [new_tile] + copy.deepcopy(curr_poly_omino)

        if new_tile[0] == -1:
            new_poly_omino = _translate_right_once(new_poly_omino)

        _rotate_and_translate_360(new_poly_omino, curr_poly_ominoes)
