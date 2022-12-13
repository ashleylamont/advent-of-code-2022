class ElevationMap:
    def __init__(self, map_string: str):
        self.map_string = map_string
        self.grid = list([[tile for tile in row] for row in map_string.splitlines(keepends=False)])
        self.flat_grid = [tile for tile in map_string.replace('\n', '')]
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.start_pos = self.flat_grid.index('S')
        self.end_pos = self.flat_grid.index('E')
        self.adjacency_map: dict[int, set[int]] = {}
        self.generate_adjacency_map()
        self.reverse_adjacency_map: dict[int, set[int]] = {}
        for tile in self.adjacency_map:
            for adj_tile in self.adjacency_map[tile]:
                if adj_tile not in self.reverse_adjacency_map:
                    self.reverse_adjacency_map[adj_tile] = set()
                self.reverse_adjacency_map[adj_tile].add(tile)

    def grid_pos(self, index_pos: int) -> (int, int):
        return index_pos % self.width, index_pos // self.width

    def index_pos(self, grid_pos: (int, int)) -> int:
        return grid_pos[0] * self.width + grid_pos[1]

    @staticmethod
    def tile_height(tile_value: str) -> int:
        if tile_value == 'S':
            return 1
        elif tile_value == 'E':
            return 26
        else:
            return ord(tile_value) - 96

    def check_tile_elevations(self, initial_tile: int, next_tile: int) -> None:
        initial_tile_value = self.flat_grid[initial_tile]
        next_tile_value = self.flat_grid[next_tile]
        if ElevationMap.tile_height(next_tile_value)\
                - ElevationMap.tile_height(initial_tile_value) <= 1:
            self.adjacency_map[initial_tile].add(next_tile)

    def generate_adjacency_map(self) -> None:
        for (index, tile) in enumerate(self.flat_grid):
            self.adjacency_map[index] = set()
            [x, y] = self.grid_pos(index)
            if x > 0:
                self.check_tile_elevations(index, index - 1)
            if x < self.width - 1:
                self.check_tile_elevations(index, index + 1)
            if y > 0:
                self.check_tile_elevations(index, index - self.width)
            if y < self.height - 1:
                self.check_tile_elevations(index, index + self.width)

    def find_path_length(self):
        explored_tiles: set[int] = set()
        unexplored_tiles: list[(int, int)] = [(0, self.start_pos)]
        while len(unexplored_tiles) > 0:
            (depth, next_tile) = unexplored_tiles.pop(0)
            if next_tile in explored_tiles:
                continue
            if next_tile == self.end_pos:
                return depth
            adjacent_tiles = self.adjacency_map[next_tile]
            for adjacent_tile in adjacent_tiles:
                unexplored_tiles.append((depth + 1, adjacent_tile))
            explored_tiles.add(next_tile)
        return -1

    def find_scenic_path_length(self):
        explored_tiles: set[int] = set()
        unexplored_tiles: list[(int, int)] = [(0, self.end_pos)]
        while len(unexplored_tiles) > 0:
            (depth, next_tile) = unexplored_tiles.pop(0)
            if next_tile in explored_tiles:
                continue
            if self.flat_grid[next_tile] == 'a':
                return depth
            adjacent_tiles = self.reverse_adjacency_map[next_tile]
            for adjacent_tile in adjacent_tiles:
                unexplored_tiles.append((depth + 1, adjacent_tile))
            explored_tiles.add(next_tile)
        return -1

