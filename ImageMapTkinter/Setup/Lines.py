def proper_lines(lines: list, angles: int):
    ls = []  # lines

    #  triangle
    if angles == 3:
        for i in range(len(lines)):
            if lines[i][0][1] != lines[i][1][1]:
                temporary = [lines[i][1], lines[i][0]]

                if temporary not in ls:
                    ls.append(lines[i])

        return ls

    # square
    for i in range(len(lines)):
        if lines[i][0][0] == lines[i][1][0]:
            temporary = [lines[i][1], lines[i][0]]

            if temporary not in ls:
                ls.append(lines[i])
    return ls
