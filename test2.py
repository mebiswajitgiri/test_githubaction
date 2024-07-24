def print_tree_pattern(height):
    # Loop through each level of the tree
    for i in range(height):
        # Print spaces for alignment
        for j in range(height - i - 1):
            print(" ", end="")
        # Print stars for the tree
        for k in range(2 * i + 1):
            print("*", end="")
        # Move to the next line
        print()

    # Print the trunk of the tree
    for i in range(height - 1):
        print(" ", end="")
    print("|")

# Example Usage:
print_tree_pattern(5)

