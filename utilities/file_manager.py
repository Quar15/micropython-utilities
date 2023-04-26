def save_file(path: str, data: str):
    with open(path, "w+") as f:
        f.write(data)

def read_file(path: str):
    with open(path, "r") as f:
        data = f.read()

    return data