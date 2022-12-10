def main():
    with open('input', 'r') as file:
        register_x = 1
        cycle = 1
        signal_strengths = []
        for line in file:
            line = line.strip()
            if line.startswith("noop"):
                cycle += 1
                if cycle % 40 == 20:
                    signal_strengths.append(register_x * cycle)
            elif line.startswith("addx"):
                cycle += 2
                if cycle % 40 == 20:
                    signal_strengths.append((register_x+int(line.split(" ")[1])) * cycle)
                elif (cycle - 1) % 40 == 20:
                    signal_strengths.append(register_x * (cycle - 1))
                register_x += int(line.split(" ")[1])
        print(sum(signal_strengths))


if __name__ == '__main__':
    main()
