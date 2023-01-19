def find_index(userDB, key: str, id: int):
    for i, dic in enumerate(userDB):
        if dic[key] == id:
            return i
    return -1