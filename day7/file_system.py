import re
from typing import List, Dict


class FileSystem:
    def __init__(self, terminal_activity: List[str]):
        self.root = {}
        self.cwd = []
        self.ls = False

        for action in terminal_activity:
            self.read_action(action)

    def __repr__(self):
        out = "- / (dir)\n"
        cwd = []

        def recurse_dirs():
            nonlocal out
            current_dir = self.get_dir(cwd)
            entries = [key for key in current_dir.keys()]
            entries.sort()
            for entry in entries:
                if isinstance(current_dir[entry], str):
                    out += f"{'  ' * len(cwd)}- {entry} (file, size={current_dir[entry]})\n"
                else:
                    out += f"{'  ' * len(cwd)}- {entry} (dir)\n"
                    cwd.append(entry)
                    recurse_dirs()
                    cwd.pop()

        recurse_dirs()

        return out

    def get_dir(self, path: list[str]) -> Dict[str, str | Dict]:
        directory = self.root
        for path_segment in path:
            directory = directory[path_segment]
        return directory

    def current_dir(self):
        return self.get_dir(self.cwd)

    def read_action(self, action: str):
        if action.startswith("$ cd"):
            self.ls = False
            self.cd(re.match(r"\$\scd\s(.+)", action).groups()[0])
        elif action.startswith("$ ls"):
            self.ls = True
        elif self.ls:
            self.read_ls(action)
        else:
            raise "Unknown terminal action"

    def cd(self, path: str):
        if path == "..":
            self.cwd.pop()
        elif path == "/":
            self.cwd = []
        else:
            current_dir = self.current_dir()
            if path not in current_dir:
                current_dir[path] = {}
            self.cwd.append(path)

    def read_ls(self, ls_result: str):
        current_dir = self.current_dir()

        if ls_result.startswith("dir"):
            new_dir_name = re.match(r"dir\s(.+)", ls_result).groups()[0]
            current_dir[new_dir_name] = {}
            return

        [size, name] = re.match(r"(\d+)\s(.+)", ls_result).groups()
        self.current_dir()[name] = size

    def total_directory_size(self, max_size: int = 100000) -> int:
        out = 0
        cwd = []

        def recurse_dirs() -> int:
            nonlocal out
            current_dir = self.get_dir(cwd)
            current_size = 0
            for entry in current_dir.keys():
                if isinstance(current_dir[entry], str):
                    current_size += int(current_dir[entry])
                else:
                    cwd.append(entry)
                    current_size += recurse_dirs()
                    cwd.pop()
            if current_size <= max_size:
                out += current_size
            return current_size

        recurse_dirs()
        return out

    def free_space_directory_size(self):
        min_space = 30000000
        available_space = 70000000
        used_space = 0
        cwd = []

        def recurse_dirs_size():
            nonlocal used_space
            current_dir = self.get_dir(cwd)
            current_size = 0
            for entry in current_dir.keys():
                if isinstance(current_dir[entry], str):
                    used_space += int(current_dir[entry])
                else:
                    cwd.append(entry)
                    recurse_dirs_size()
                    cwd.pop()
            return current_size

        recurse_dirs_size()

        free_space = available_space - used_space
        needed_space = min_space - free_space

        smallest_directory_size = 0

        def recurse_dirs_find_min() -> int:
            nonlocal smallest_directory_size
            current_dir = self.get_dir(cwd)
            current_size = 0
            for entry in current_dir.keys():
                if isinstance(current_dir[entry], str):
                    current_size += int(current_dir[entry])
                else:
                    cwd.append(entry)
                    current_size += recurse_dirs_find_min()
                    cwd.pop()
            if current_size >= needed_space and \
                    (smallest_directory_size == 0 or current_size < smallest_directory_size):
                smallest_directory_size = current_size
            return current_size

        recurse_dirs_find_min()

        return smallest_directory_size


