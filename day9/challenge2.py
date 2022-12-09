from day9.rope_pair import RopePair


def main():
    with open('input', 'r') as file:
        head = RopePair()
        tail = head
        for i in range(8):
            new_tail = RopePair()
            tail.add_chained(new_tail)
            tail = new_tail

        tail_path = set()

        def trail():
            nonlocal tail
            nonlocal tail_path
            tail_path.add((tail.tail[0], tail.tail[1]))

        trail()

        for line in file:
            [direction, distance] = line.strip().split(' ')
            for iteration in range(int(distance)):
                # Move head
                if direction == 'R':
                    head.move_head(1, 0)
                elif direction == 'L':
                    head.move_head(-1, 0)
                elif direction == 'U':
                    head.move_head(0, 1)
                else:
                    head.move_head(0, -1)

                trail()
        print(len(tail_path))


if __name__ == "__main__":
    main()
