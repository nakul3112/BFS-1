# Time Complexity (BFS Approach) :
# O(N)

# Space Complexity (BFS Approach):  
# O(N)


# Approach:
# ==> We can have two approaches. One is Queue based BFS approach and another is DFS approach.
# ==> For Queue based approach, we initiate a queue, which is supposed to hold the nodes at same level.
# ==> Then for each node in current queue, we add their left and right child nodes, after adding the node's value
#     itself to the "levelList" which hold the node values for that level
# ==> Then we add this levelList to the result after we traversed all the nodes in queue, which we captured by 
#     keeping track of size of the queue before beginning the exploration of child nodes.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # ==========> Approach 1:  Using Queue , TC ==> O(n), SC ===> O(n)  <=========== #

    def levelOrder(self, root):
        if not root:
            return
        
        result = []   # list of list to hold the elements from level-order traversal
        queue = []   #queue to hold level-wise nodes
        queue.append(root)

        while (queue):
            q = len(queue)
            levelList = []    # list to hold node values from same level
            for i in range(0,q):
                currNode = queue.pop(0)
                levelList.append(currNode.val)  # add node's value to list for current level

                if (currNode.left):
                    queue.append(currNode.left)

                if (currNode.right):
                    queue.append(currNode.right)
            
            result.append(levelList)

        return result





class Solution(object):

    # =====> Approach 2:  DFS based Approach with Level Tracking  ,TC ==> O(n), SC ===> O(h), where h = height of tree

    def __init__(self):
        self.result = []    #List of list to store level order elements

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return

        self.dfs(root, 0)
        print("Printning the result list here: ", self.result)
        return self.result


    def dfs(self, root , lvl):
        if not root:
            return
        
        # check if you found "lvl" for first time
        if lvl == len(self.result):
            #print("Level encountered for first time:")
            levelList = []
            self.result.append(levelList)
            #print("Printning the result list here: ", self.result)

        # add node value to the list at index "lvl"
        self.result[lvl].append(root.val)

        #recurssive left subtree
        self.dfs(root.left, lvl+1)

        #recurssive right subtree
        self.dfs(root.right, lvl+1)


