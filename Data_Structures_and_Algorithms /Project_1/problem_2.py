from os import path, listdir


def find_files(suffix, file_path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result = []
    if path.isfile(file_path):
        if is_file_in_path(suffix, file_path):
            result.append(path.basename(file_path))
    elif path.isdir(file_path):
        for f_path in listdir(file_path):
            prev_result = find_files(suffix, f"{file_path}/{f_path}")
            result.extend(prev_result)

    return result

def is_file_in_path(suffix, file_path):
    return file_path.endswith(suffix)

result = find_files(".c", "/Users/temitayooyelowo/Desktop/Udacity_Nanodegree/Project_1/testdir")
print(result)