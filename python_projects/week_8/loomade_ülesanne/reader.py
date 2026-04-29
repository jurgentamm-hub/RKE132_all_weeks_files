from  utils import clean_list

def read_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = clean_list(f.readlines())
    return data
