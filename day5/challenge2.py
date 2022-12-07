import re


def print_stacks(stacks):
    total_height = max(map(lambda stack: len(stack), stacks))
    for row in range(total_height - 1, -1, -1):
        row_out = ''
        for stack_number in range(len(stacks)):
            stack = stacks[stack_number]
            if len(stack) > row:
                row_out += f'[{stack[row]}] '
            else:
                row_out += '    '
        print(row_out)
    out = ''
    for stack_number in range(len(stacks)):
        out += f' {stack_number+1}  '
    print(out)
    print()


def main():
    with open('input', 'r') as file:
        stacks = []

        is_reading_stacks = True

        for line in file:
            line = line.replace('\n', '')
            if line == '':
                is_reading_stacks = False
                print_stacks(stacks)
            elif is_reading_stacks:
                # Ignore the numbers line, we'll read the stack numbers as positional
                if not all(map(lambda char: char.isnumeric() or char == ' ', line)):
                    for stack_number in range(0, (len(line) + 1) // 4):
                        if line[stack_number * 4] == '[':
                            # Crate exists in stack
                            if len(stacks) > stack_number:
                                stacks[stack_number].insert(0, line[stack_number * 4 + 1])
                            else:
                                stacks.append([line[stack_number * 4 + 1]])
                        else:
                            # No crate but make a stack anyways
                            if len(stacks) <= stack_number:
                                stacks.append([])
            else:
                instructions = re.match(r'^move (\d+) from (\d+) to (\d+)$', line)
                [quantity, from_stack, to_stack] = map(lambda x: int(x) - 1, instructions.groups())
                quantity += 1  # Offset the decrement above
                temp_stack = []
                for i in range(quantity):
                    temp_stack.append(stacks[from_stack].pop())
                for i in range(quantity):
                    stacks[to_stack].append(temp_stack.pop())
                print_stacks(stacks)
        for stack in stacks:
            print(stack[len(stack)-1], end='')
        print()


if __name__ == '__main__':
    main()
