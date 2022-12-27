x = [8, 0, 3, 4, 1, 8, 8, 10, 7]

def deleted_Duplicates(itemes):
    y = []
    for item in itemes:
        if item not in y:
            y.append(item)

    return y

print(deleted_Duplicates(x))

