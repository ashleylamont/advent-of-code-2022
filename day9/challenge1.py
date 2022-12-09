from day9.rope_pair import RopePair


def main():
    with open('input', 'r') as file:
        rope_pair = RopePair()
        tail_path = set()

        def trail():
            nonlocal rope_pair
            nonlocal tail_path
            tail_path.add((rope_pair.tail[0], rope_pair.tail[1]))

        trail()

        for line in file:
            [direction, distance] = line.strip().split(' ')
            for iteration in range(int(distance)):
                # Move head
                if direction == 'R':
                    rope_pair.move_head(1, 0)
                elif direction == 'L':
                    rope_pair.move_head(-1, 0)
                elif direction == 'U':
                    rope_pair.move_head(0, 1)
                else:
                    rope_pair.move_head(0, -1)

                trail()
        print(len(tail_path))


if __name__ == "__main__":
    main()
