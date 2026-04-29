
def use_write_mode(file_path):

    with open(file_path, "w", encoding='utf-8') as f:
        pass

use_write_mode(r"week_9\data\todo.txt")