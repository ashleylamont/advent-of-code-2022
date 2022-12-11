import re
from typing import Callable


class Monkey:
    def __init__(self, monkey_description: str, throw: Callable[[str, int], None],
                 part2: bool = False):
        self.id = re.search(r"Monkey (\d+):", monkey_description, re.MULTILINE).group(1)
        self.items = list(map(lambda x: int(x), re.search(r"Starting items: (\d+(?:,\s\d+)*)",
                                                          monkey_description).group(1).split(", ")))
        self.operation = re.search(r"Operation: ([a-z]+) = ([a-z0-9]+) (.) ([a-z0-9]+)",
                                   monkey_description).groups()
        self.test = int(re.search(r"Test: divisible by (\d+)", monkey_description).group(1))
        self.true_case = re.search(r"If true: throw to monkey (\d+)", monkey_description).group(1)
        self.false_case = re.search(r"If false: throw to monkey (\d+)", monkey_description).group(1)
        self.throw = throw
        self.inspections = 0
        self.part2 = part2

    def inspect_next_item(self):
        self.inspections += 1

        # Do the initial operation
        val1_text = self.operation[1]
        operator_text = self.operation[2]
        val2_text = self.operation[3]

        item = self.items.pop(0)

        if val1_text == 'old':
            val1 = item
        else:
            raise ValueError(f"Invalid val1 input '{val1_text}'.")
        if val2_text == 'old':
            val2 = item
        elif val2_text.isnumeric():
            val2 = int(val2_text)
        else:
            raise ValueError(f"Invalid val2 input '{val2_text}'.")

        mod_factor = 2*17*19*3*5*13*7*11

        if operator_text == '+':
            item = ((val1 % mod_factor) + (val2 % mod_factor)) % mod_factor
        elif operator_text == '*':
            item = ((val1 % mod_factor) * (val2 % mod_factor)) % mod_factor
        else:
            raise ValueError(f"Invalid operator input '{operator_text}'.")

        # Worry level //= 3
        if not self.part2:
            item = item // 3

        # Do test to throw
        if item % self.test == 0:
            # Do true case
            self.throw(self.true_case, item)
        else:
            # Do false case
            self.throw(self.false_case, item)

    def do_turn(self):
        while len(self.items) > 0:
            self.inspect_next_item()
