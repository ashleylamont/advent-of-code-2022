def main():
    trees = []
    with open('input', 'r') as file:
        for line in file:
            line = line.strip()
            trees.append(list(line))

    width = len(trees[0])
    flat_trees = [tree for tree_row in trees for tree in tree_row]
    num_visible = 0
    for row_num, tree_row in enumerate(trees):
        for col_num, tree in enumerate(tree_row):
            visible = False
            if col_num == width - 1 or col_num == 0:
                visible = True
            elif row_num == 0 or row_num == len(trees) - 1:
                visible = True
            else:
                tree_index = row_num * width + col_num
                visible_top = all([flat_trees[i] < tree for i in
                                   range(tree_index - width, -1, -width)])
                visible_left = all([flat_trees[i] < tree for i in
                                    range(tree_index - 1, (tree_index - tree_index % width) - 1,
                                          -1)])
                visible_right = all([flat_trees[i] < tree for i in
                                     range(tree_index + 1,
                                           (tree_index - tree_index % width) + width)])
                visible_bottom = all([flat_trees[i] < tree for i in
                                      range(tree_index + width, len(flat_trees), width)])
                if visible_bottom or visible_right or visible_left or visible_top:
                    visible = True
            if visible:
                print(tree, end='')
                num_visible += 1
            else:
                print('\u2591', end='')
        print()
    print(num_visible)


if __name__ == "__main__":
    main()
