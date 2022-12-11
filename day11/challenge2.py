from typing import List

from day11.monkey import Monkey


def main():
    with open('input', 'r') as file:
        monkey_descriptions = file.read().split('\n\n')
        monkeys: List[Monkey] = []

        def throw(monkey_id: str, item: int) -> None:
            target_monkey = [searched_monkey for searched_monkey in monkeys
                             if searched_monkey.id == monkey_id][0]
            target_monkey.items.append(item)

        for monkey_description in monkey_descriptions:
            monkey = Monkey(monkey_description, throw, True)
            monkeys.append(monkey)

        for i in range(10000):
            if (i+1) % 100 == 0:
                print(f"{('#' * ((i+1) // 100)):_<100} ({(i+1)}/10000)")
            for monkey in monkeys:
                monkey.do_turn()

        monkey_business = list(map(lambda m: m.inspections, monkeys))
        print(monkey_business)
        monkey_business.sort(reverse=True)
        print(monkey_business[0] * monkey_business[1])


if __name__ == '__main__':
    main()
