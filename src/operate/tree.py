# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def traverse(self, root):
        """
        递归遍历 -> DFS
        """
        if root is None:
            return

        # 前序遍历
        self.traverse(root.left)
        # 中序遍历
        self.traverse(root.right)
        # 后序遍历

    def levelOrderTraverse1(self, root):
        """
        层序遍历 -> BFS
        第一种
        """
        if root is None:
            return

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            print(node.val)  # 执行操作

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def levelOrderTraverse2(self, root):
        """
        层序遍历 -> BFS
        第二种：记录深度
        """
        if root is None:
            return

        q = deque()
        q.append(root)
        depth = 1

        while q:
            size = len(q)  # 记录当前层数的节点数，方便后续整层连续遍历
            for i in range(size):
                node = q.popleft()
                print(f"depth = {depth}, val = {node.val}")  # 执行操作
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1  # 当前层遍历完成，深度加1

    def levelOrderTraverse2(self, root):
        """
        层序遍历 -> BFS
        第三种：引入State类，可记录每个节点的深度
        """
        if root is None:
            return

        q = deque()
        q.append(State(root, 1))

        while q:
            cur = q.popleft()
            print(f"depth = {cur.depth}, val = {cur.node.val}")  # 执行操作

            if cur.node.left:
                q.append(State(cur.node.left, cur.depth + 1))
            if cur.node.right:
                q.append(State(cur.node.right, cur.depth + 1))


class State(object):
    def __init__(self, node: TreeNode, depth):
        self.node = TreeNode
        self.depth = depth


## 前序遍历二叉树的值
class Solution:
    # 方式1：回溯算法，设置变量存取val
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(root: TreeNode):
            if root is None:
                return
            nonlocal res
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return res

    ## 方式2: 动态规划，分解子问题
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res


# 二叉树最大深度
class Solution:

    ## 方式1：动态规划，分解成下级子树的最大深度，递归求解
    ## 时间复杂度：O(n)，空间复杂度：O(n)
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

    ## 方式2：回溯算法 ，计算每个节点的深度，然后求最大值
    def maxDepth(self, root: TreeNode) -> int:
        res = 0
        depth = 0

        def helper(root: TreeNode):
            if root is None:
                return
            nonlocal depth, res  # 声明使用外部变量

            depth += 1
            if root.left is None and root.right is None:
                res = max(res, depth)

            helper(root.left)
            helper(root.right)
            # 返回到上一级，深度需要减一
            depth -= 1

        helper(root)
        return res


## 延伸：二叉树节点总数 | 二叉树每个节点的左右子树各有多少节点
def count(root: TreeNode):
    if root is None:
        return 0
    ## 下面返回时计算左右子树节点总数，计算二叉树节点总数还要算上根节点，即再+1
    return 1 + count(root.left) + count(root.right)


## 二叉树直径：即树中任意两个节点之间最长路径的长度（跳数）
## 也算一个二叉树深度的延伸
class Solution:
    # 动态规划：左右子树的深度的和即为二叉树的直径
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maxPath = 0

        def helper(root: TreeNode) -> int:
            if root is None:
                return 0
            nonlocal maxPath
            left_depth = helper(root.left)
            right_depth = helper(root.right)
            maxPath = max(maxPath, left_depth + right_depth)

        helper(root)
        return maxPath


## 二叉树寻找重复子树
# 序列化+动态规划
# 可以将一棵以 x 为根节点值的子树序列化为：x(左子树的序列化结果)(右子树的序列化结果)
# 左右子树分别递归地进行序列化。如果子树为空，那么序列化结果为空: 1(2(4()())())(3(2(4()())())(4()()))
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode):
        res = set()
        repeat = {}

        def helper(root: TreeNode):
            if root is None:
                return ""
            left_serial = helper(root.left)
            right_serial = helper(root.right)

            # x(左子树的序列化结果)(右子树的序列化结果)
            serial = "".join(
                str(root.val), "(", left_serial, ")", "(", right_serial, ")"
            )
            # 必须使用原来的node，否则新的和原来的引用不一样，set会认为是两个，无法去重
            if serial in repeat:
                res.add(repeat[serial])
            else:
                repeat[serial] = root

            return serial

        helper(root)

        return list(res)
