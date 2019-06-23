from os import path, listdir, getcwd

class FileFinder:

    def find_files(self, suffix, file_path):
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

        # Inner function
        def is_file_in_path(self, suffix, file_path):
            return file_path.endswith(suffix)

        if path.isfile(file_path):
            if self.is_file_in_path(suffix, file_path):
                result.append(path.basename(file_path))
        elif path.isdir(file_path):
            for f_path in listdir(file_path):
                prev_result = self.find_files(suffix, f"{file_path}/{f_path}")
                result.extend(prev_result)

        return result

# file_finder = FileFinder()
# result = file_finder.find_files(".c", f"{getcwd()}/testdir")
# print(result)