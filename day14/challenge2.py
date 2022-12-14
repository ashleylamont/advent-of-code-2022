import time

from day14.cave import Cave


def main():
    with open('input', 'r') as file:
        cave = Cave()
        for line in file:
            cave.read_rock_path(line)

        sand_count = 1
        sand = cave.add_sand_part_2()
        while sand:
            sand_count += 1
            sand = cave.add_sand_part_2()
        print(cave)
        print(sand_count)


if __name__ == "__main__":
    main()
