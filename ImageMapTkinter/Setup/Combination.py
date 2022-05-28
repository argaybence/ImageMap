def combine(elements: list, duplicate=True):
    out_list = []
    if duplicate:
        for i in range(len(elements)):
            for j in range(len(elements)):
                out_list.append([elements[i], elements[j]])
        return out_list

    for i in range(len(elements)):
        for j in range(len(elements)):
            if elements[i] != elements[j]:
                out_list.append([elements[i], elements[j]])
    return out_list
