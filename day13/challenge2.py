import functools
import inspect
import json

DEBUG = False
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


def compare_packets(left_packet, right_packet):
    if is_list_pair_valid(left_packet, right_packet):
        return -1
    return 1

def main():
    global base_stack_level
    with open('input', 'r') as file:
        packets = [json.loads(data) for data in file.read().replace('\n\n', '\n').splitlines(keepends=False)]
        packets.append([[2]])
        packets.append([[6]])
        packets.sort(key=functools.cmp_to_key(compare_packets))
        # print('\n'.join(map(lambda p: json.dumps(p), packets)))
        print((packets.index([[2]])+1) * (packets.index([[6]])+1))


if __name__ == "__main__":
    main()
