import os


def find_files(suffix, path):
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
    if not suffix or not path:
        print(f"Suffix and path should have a avlue")
        return None

    def get_matched_files(suffix, path, matched_files=list()):

        path_content = os.scandir(path)

        for entry in path_content:

            if entry.is_file() and entry.path.endswith(suffix):
                matched_files.append(entry.path)
                return matched_files

            # recursively call sub directory and check for its content
            if entry.is_dir():
                get_matched_files(suffix, entry.path, matched_files)

    try:
        matched_files = get_matched_files(suffix, path)

        if matched_files:
            print(*matched_files, sep="\n")
            return matched_files

        print("Couldn't find any match")
        return None

    except OSError as oserr:
        print(f"An error occured: {oserr}")
        return None
