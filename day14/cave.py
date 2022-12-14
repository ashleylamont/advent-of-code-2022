from day14.tile import Tile


class Cave:
    def __init__(self):
        self.grid: dict[tuple[int, int], Tile] = {(500, 0): Tile.SOURCE}
        self.cached_kill_y: int | None = None

    def read_rock_path(self, rock_path_description: str) -> None:
        points: list[tuple[int, ...]] = [tuple(map(lambda x: int(x), point.split(',')))
                                         for point in rock_path_description.strip().split(' -> ')]
        last_point = points[0]
        for (nx, ny) in points:
            (px, py) = last_point
            for x in range(min(px, nx), max(px, nx) + 1):
                for y in range(min(py, ny), max(py, ny) + 1):
                    self.grid[(x, y)] = Tile.ROCK
            last_point = (nx, ny)

        self.cached_kill_y = None

    def __str__(self):
        min_x = 10e3
        max_x = 0
        min_y = 10e3
        max_y = 0

        for (x, y) in self.grid:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

        out = ""
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) in self.grid:
                    out += str(self.grid[(x, y)])
                else:
                    out += "."
            out += "\n"

        return out

    def get_tile(self, x: int, y: int) -> Tile:
        if (x, y) in self.grid:
            return self.grid[(x, y)]
        return Tile.AIR

    @property
    def kill_y(self):
        if self.cached_kill_y is not None:
            return self.cached_kill_y

        max_y = 0

        for (_, y) in self.grid:
            max_y = max(max_y, y)

        self.cached_kill_y = max_y

        return max_y

    def add_sand(self) -> bool:
        sand_pos = [500, 0]
        while sand_pos[1] < self.kill_y:
            below_tile = self.get_tile(sand_pos[0], sand_pos[1] + 1)
            if below_tile == Tile.AIR:
                sand_pos[1] += 1
                continue

            below_left_tile = self.get_tile(sand_pos[0] - 1, sand_pos[1] + 1)
            if below_left_tile == Tile.AIR:
                sand_pos[0] -= 1
                sand_pos[1] += 1
                continue

            below_right_tile = self.get_tile(sand_pos[0] + 1, sand_pos[1] + 1)
            if below_right_tile == Tile.AIR:
                sand_pos[0] += 1
                sand_pos[1] += 1
                continue

            break

        if sand_pos[1] < self.kill_y:
            self.grid[(sand_pos[0], sand_pos[1])] = Tile.SAND
            return True

        return False

    def add_sand_part_2(self) -> bool:
        sand_pos = [500, 0]
        while sand_pos[1] < self.kill_y + 1:
            below_tile = self.get_tile(sand_pos[0], sand_pos[1] + 1)
            if below_tile == Tile.AIR:
                sand_pos[1] += 1
                continue

            below_left_tile = self.get_tile(sand_pos[0] - 1, sand_pos[1] + 1)
            if below_left_tile == Tile.AIR:
                sand_pos[0] -= 1
                sand_pos[1] += 1
                continue

            below_right_tile = self.get_tile(sand_pos[0] + 1, sand_pos[1] + 1)
            if below_right_tile == Tile.AIR:
                sand_pos[0] += 1
                sand_pos[1] += 1
                continue

            break

        if sand_pos[0] == 500 and sand_pos[1] == 0:
            self.grid[(sand_pos[0], sand_pos[1])] = Tile.SAND
            return False

        self.grid[(sand_pos[0], sand_pos[1])] = Tile.SAND
        return True

