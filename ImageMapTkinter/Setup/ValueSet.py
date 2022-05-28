def value_set(coords: list):
    y_axis = []

    for i in range(len(coords)):
        y_axis.append(coords[i][0][1])
        y_axis.append(coords[i][1][1])

    return min(y_axis), max(y_axis)
