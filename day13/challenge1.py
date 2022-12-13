import inspect
import json

DEBUG = True
base_stack_level = 0


def log(message):
    if DEBUG:
        print(f"{' ' * (len(inspect.stack(0)) - base_stack_level)}- {message}")


def is_int_pair_valid(left_int: int | None, right_int: int | None) -> bool | None:
    log(f"Compare {left_int} vs {right_int} (iipv)")
    if left_int is None and right_int is None:
        return None
    elif left_int is None and right_int is not None:
        log("Left side ran out of items, so inputs are in the right order.")
        return True
    elif left_int is not None and right_int is None:
        log("Right side ran out of items, so inputs are not in the right order.")
        return False
    elif left_int < right_int:
        log("Left side is smaller, so inputs are in the right order.")
        return True
    elif right_int < left_int:
        log("Right side is smaller, so inputs are not in the right order.")
        return False


def is_list_pair_valid(left_list: list, right_list: list):
    log(f"Compare {left_list} vs {right_list} (ilpv)")
    comparison_index = 0
    while comparison_index < len(left_list) and comparison_index < len(right_list):
        left_data = left_list[comparison_index]
        right_data = right_list[comparison_index]
        comparison_result = is_data_pair_valid(left_data, right_data)
        if comparison_result:
            return True
        elif not comparison_result and comparison_result is not None:
            return False
        comparison_index += 1
    if len(left_list) < len(right_list):
        log("Left side ran out of items, so inputs are in the right order.")
        return True
    if len(right_list) < len(left_list):
        log("Right side ran out of items, so inputs are not in the right order.")
        return False
    return None


def is_data_pair_valid(left_data: int | list, right_data: int | list) -> bool | None:
    log(f"Compare {left_data} vs {right_data} (idpv)")
    if type(left_data) == type(right_data) == int:
        return is_int_pair_valid(left_data, right_data)
    elif type(left_data) == type(right_data) == list:
        return is_list_pair_valid(left_data, right_data)
    elif type(left_data) == int and type(right_data) == list:
        return is_list_pair_valid([left_data], right_data)
    elif type(left_data) == list and type(right_data) == int:
        return is_list_pair_valid(left_data, [right_data])


def main():
    global base_stack_level
    with open('input', 'r') as file:
        pairs = file.read().split('\n\n')
        total = 0
        for (pair_idx, pair_str) in enumerate(pairs):
            packet_pair = [json.loads(packet) for packet in pair_str.strip().split('\n')]
            [left_packet, right_packet] = packet_pair
            base_stack_level = len(inspect.stack(0)) + 2
            if DEBUG:
                print(f"\n\n== Pair {pair_idx + 1} ==")
            if is_list_pair_valid(left_packet, right_packet):
                print(f"Valid on pair {pair_idx + 1}")
                total += pair_idx + 1
        print(total)


if __name__ == "__main__":
    main()
