def coordinate_translater(geometry: tuple, coord: tuple):
    reduce_x = geometry[0] // 2
    reduce_y = geometry[1] // 2

    if coord[1] > reduce_y:
        return coord[0] - reduce_x, -(coord[1] - reduce_y)
    return coord[0] - reduce_x, abs(coord[1] - reduce_y)
