# Recursive solution (slower than iterative solution but simpler; uses call stack)

def walk(tree):
    if tree is not None:
        # The node itself is printed before its children, so this is preorder
        # print(tree)
        walk(tree.left)
        # Inorder traversal
        # print(tree)
        walk(tree.right)
        # Postorder traversal
        # print(tree)

# Iterative solution (faster but more complex to understand)

def walk2(tree, stack):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            # Traversal method can change as above depending on where print statement is
            print(node)
            # Because stacks are in reverse order, add right first then left
            stack.append(node.right)
            stack.append(node.left)