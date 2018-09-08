def read_files(filename):
    """open settings in disk"""
    read_filename = filename
    contents = []
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            line = str(line)
            line = line.strip()
            contents.append(line)
    return contents

def if_fuc(col_if_s, col_if_y, col_if_ye,
    col_compute_s, col_compute_y, col_compute_ye):
    """if function for apply"""
    if col_if_s != 0:
        out = col_compute_s / col_if_s
        return out
    elif col_if_y != 0:
        out = col_compute_y / col_if_y
        return out
    else:
        out = col_compute_ye / col_if_ye
        return out
