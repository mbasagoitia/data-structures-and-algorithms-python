from collections import deque
from collections import List
 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        res = []
        # Initialize a queue using the deque data structure
        q = deque()
        # Add the root node to the queue
        q.append(root)

        # While there are still nodes left in the queue, loop through the entire queue,
        # read its data (in this case, push it to a new level list) and enqueue its children in left, right order
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                # Node could be null
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # In this implementation, then also add the level to the results array if it is not empty
            if level:
                res.append(level)
        
        return res
    

def bfs(tree):
    if not tree:
        return
    
    q = deque([tree])  # Initialize queue with the root node
    
    while q:
        qLen = len(q)  # Number of nodes at the current level
        for _ in range(qLen):
            node = q.popleft()  # Remove and retrieve the front node
            print(node.value)  # Process the node
            if node.left:  # Add left child to queue if it exists
                q.append(node.left)
            if node.right:  # Add right child to queue if it exists
                q.append(node.right)
