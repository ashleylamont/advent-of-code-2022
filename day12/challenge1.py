from day12.elevation_map import ElevationMap


def main():
    with open('input', 'r') as file:
        elevation_map = ElevationMap(file.read().strip())
        print(elevation_map.find_path_length())


if __name__ == "__main__":
    main()
