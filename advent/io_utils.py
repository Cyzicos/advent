def load_txt(path):
    with open(path) as f:
        content = f.readlines()
    return content
