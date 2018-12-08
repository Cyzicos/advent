def load_txt(path):
    with open(path) as f:
        content = f.readlines()
    content = [i.strip() for i in content]
    return content
