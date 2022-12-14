import time

from day14.cave import Cave


def main():
    with open('test_input', 'r') as file:
        cave = Cave()
        for line in file:
            cave.read_rock_path(line)

        sand_count = 0
        sand = cave.add_sand()
        while sand:
            sand_count += 1
            sand = cave.add_sand()
        print(cave)
        print(sand_count)


if __name__ == "__main__":
    main()
