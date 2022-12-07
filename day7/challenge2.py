from day7.file_system import FileSystem


def main():
    with open("input", "r") as file:
        fs = FileSystem(file.readlines())
        print(fs.free_space_directory_size())


if __name__ == "__main__":
    main()
