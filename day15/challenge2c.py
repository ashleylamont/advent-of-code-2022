import re
from timeit import default_timer


def main():
    with open('input', 'r') as file:
        input_size = 4000000
        edges: list[((int, int), (int, int))] = []
        sensors: list[((int, int), int)] = []
        for line in file:
            input_data = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at "
                                  r"x=(-?\d+), y=(-?\d+)", line.strip()).groups()
            [sensor_x, sensor_y, beacon_x, beacon_y] = map(int, input_data)
            sensor_range = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y) + 1
            sensors.append(((sensor_x, sensor_y), sensor_range-1))
            left_corner = (sensor_x - sensor_range, sensor_y)
            top_corner = (sensor_x, sensor_y + sensor_range)
            right_corner = (sensor_x + sensor_range, sensor_y)
            bottom_corner = (sensor_x, sensor_y - sensor_range)
            edges.append((left_corner, top_corner))
            edges.append((top_corner, right_corner))
            edges.append((right_corner, bottom_corner))
            edges.append((bottom_corner, left_corner))

        intersections: set[(int, int)] = set()
        for edge_a in edges:
            (point_aa, point_ab) = edge_a
            (xaa, yaa) = point_aa
            (xab, yab) = point_ab
            ma = (yab - yaa) // (xab - xaa)
            # y - y1 = m(x - x1)
            # y = m(x - x1) + y1
            # y = mx + (y1 - m*x1)
            ba = yaa - ma * xaa
            for edge_b in edges:
                (point_ba, point_bb) = edge_b
                (xba, yba) = point_ba
                (xbb, ybb) = point_bb
                mb = (ybb - yba) // (xbb - xba)
                bb = yba - mb * xba

                # ma * x + ba = mb * x + bb
                # ma * x - mb * x = bb - ba
                # (ma - mb) * x = bb - ba
                # x = (bb - ba) / (ma - mb)
                if ma == mb:
                    continue
                x_intercept = (bb - ba) // (ma - mb)
                y_intercept = ma * x_intercept + ba
                if 0 <= x_intercept <= input_size and 0 <= y_intercept <= input_size:
                    intersections.add((x_intercept, y_intercept))

        for intersection in intersections:
            for (sensor_position, sensor_range) in sensors:
                if abs(intersection[0] - sensor_position[0]) + abs(intersection[1] - sensor_position[1]) <= sensor_range:
                    break
            else:
                print(intersection)
                print(intersection[0] * 4000000 + intersection[1])


if __name__ == '__main__':
    start = default_timer()
    main()
    print(str((default_timer() - start)*1000) + "ms")
