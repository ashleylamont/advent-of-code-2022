def main():
    with open('input', 'r') as file:
        register_x = 2
        cycle = 1

        def mid_cycle():
            print('#' if abs(cycle % 40 - register_x) <= 1 else '.',
                  end=('\n' if cycle % 40 == 0 else ''))

        for line in file:
            line = line.strip()
            if line.startswith("noop"):
                mid_cycle()
                cycle += 1
            elif line.startswith("addx"):
                mid_cycle()
                cycle += 1
                mid_cycle()
                cycle += 1
                register_x += int(line.split(" ")[1])


if __name__ == '__main__':
    main()
