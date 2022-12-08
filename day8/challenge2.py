def main():
    trees = []
    with open('input', 'r') as file:
        for line in file:
            line = line.strip()
            trees.append(list(line))

    width = len(trees[0])
    flat_trees = [tree for tree_row in trees for tree in tree_row]
    best_score = 0
    for row_num, tree_row in enumerate(trees):
        for col_num, tree in enumerate(tree_row):
            tree_index = row_num * width + col_num
            top_trees = range(tree_index - width, -1, -width)
            left_trees = range(tree_index - 1, (tree_index - tree_index % width) - 1, -1)
            right_trees = range(tree_index + 1, (tree_index - tree_index % width) + width)
            bottom_trees = range(tree_index + width, len(flat_trees), width)

            def count_visible(tree_indices):
                nonlocal tree
                nonlocal flat_trees
                visible = 0
                for next_tree in tree_indices:
                    if flat_trees[next_tree] < tree:
                        visible += 1
                    else:
                        return visible + 1
                return visible

            tree_score = count_visible(left_trees) * count_visible(right_trees) * count_visible(bottom_trees) * count_visible(top_trees)
            if tree_score > best_score:
                best_score = tree_score

    print(best_score)


if __name__ == "__main__":
    main()
