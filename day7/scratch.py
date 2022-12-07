from day7.file_system import FileSystem

with open('input', 'r') as file:
    lines = file.readlines()
    fs = FileSystem(lines)
    print(fs)
