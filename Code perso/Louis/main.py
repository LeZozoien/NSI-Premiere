def get_default(path)->list:
    with open(str(path), 'r+') as file:
        test = file.read().splitlines()
    return test

def write_default(path, default):
    with open(str(path), 'w+') as file:
        file.writelines([str(data)+"\n" for data in default])

