from typing import List
from functools import reduce


class ListNode(object):
    """
    list struct
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTwoLists(self, L1: ListNode, L2: ListNode):
        """
        21. 合并两个有序链表
        """
        if not L1:
            return L2
        if not L2:
            return L1

        head = ListNode(0)
        node = head
        while L1 and L2:
            if L1.val < L2.val:
                node.next = L1
                L1 = L1.next
            else:
                node.next = L2
                L2 = L2.next
            node = node.next

        if L1:
            node.next = L1
        else:
            node.next = L2
        return head.next

    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        86. 分隔链表
        """
        h0 = h1 = ListNode()
        h2 = h3 = ListNode()

        while head:
            if head.val < x:
                h1.next = head
                h1 = h1.next
            else:
                h2.next = head
                h2 = h2.next
            head = head.next
        h2.next = None  # 必须给末尾断开，否则容易成环，造成超时
        h1.next = h3.next

        return h0.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        23. 合并K个升序链表
        """
        if not lists:
            return None

        # res = []
        # for list in lists[1:]:
        #     res = self.mergeTwoLists(res, list)
        return reduce(self.mergeTwoLists, lists)

    def trainingPlan(self, head: ListNode, cnt: int) -> ListNode:
        """
        140. 链表的中间结点
        """
        # len = 0
        # tmp = head
        # while tmp.next:
        #     tmp = tmp.next
        #     len += 1

        # for i in range(len - cnt + 1):
        #     head = head.next

        # return head
        p1 = head
        for i in range(cnt):  # 找到第k个节点
            p1 = p1.next

        p2 = head
        while p1:  # 同时走n-k步
            p1 = p1.next
            p2 = p2.next
        # p2为第k个节点
        return p2

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        19. 删除链表的倒数第 N 个结
        倒数第n个节点 = 链表长度 - n + 1
        """
        dummy = ListNode(0, head)
        first = head
        second = dummy  # 慢指针多一个dummy节点
        for i in range(n):  # 找到第n个节点
            first = first.next

        while first:  #
            first = first.next
            second = second.next
        # p2为第k个节点的前一个节点
        second.next = second.next.next

        return dummy.next

    def middleNode(self, head: ListNode) -> ListNode:
        """ "
        876. 链表的中间结点
        fast = 2 * slow
        """
        if not head:
            return
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def hasCycle(self, head: ListNode) -> bool:
        """
        141. 环形链表
        """
        # 方法一：快慢指针
        # if not head or not head.next:
        #     return False

        # fast = slow = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False

        # 方法2：哈希表
        if not head or not head.next:
            return False
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        # 方法一：快慢指针
        # fast = slow = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         break
        # if not fast or not fast.next:
        #     return None

        # slow = head
        # while slow != fast:
        #     slow = slow.next
        #     fast = fast.next
        # return slow

        # 方法2：哈希表
        seen = set()
        while head:
            if head in seen:
                break
            seen.add(head)
            head = head.next
        if not head:
            return None
        return head

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        160. 相交链表
        """
        # 方法1：哈希表，空间复杂度O(n)，可能不符合要求
        # seen = set()
        # while headA:
        #     seen.add(headA)

        # while headB:
        #     if headB in seen:
        #         break
        # if not headB:
        #     return None
        # return headB

        # 方法2：双指针
        h1, h2 = headA, headB
        while h1 != h2:
            h1 = headB if not h1 else h1.next
            h2 = headA if not h2 else h2.next
        return h1

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        83. 删除排序链表中的重复元素
        """
        if not head:
            return None
        slow, fast = head, head.next
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next

            fast = fast.next
        slow.next = None
        return head

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        26. 删除排序数组中的重复项
        """

        if not nums:
            return 0
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                if (fast - slow) > 0:
                    nums[slow] = nums[fast]
            fast += 1

        return slow + 1

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        27. 移除元素
        """
        if not nums:
            return 0

        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        167. 两数之和 II - 输入有序数组
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left + 1, right + 1]
            elif res < target:
                left += 1
            else:
                right -= 1

        return []

    def minWindow(self, s: str, t: str) -> str:
        """
        76. 最小覆盖子串
        """
        need, window = {}, {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        right, left = 0, 0
        valid = 0
        start, length = 0, float("inf")  # 记录起始位置
        while right < len(s):
            # 外层while扩大窗口
            c = s[right]
            right += 1
            if c in need:
                # 记录c字符的数量
                window[c] = window.get(c, 0) + 1
                if need[c] == window[c]:
                    valid += 1

            while valid == len(need):  # 窗口缩小时机：窗口内字符数与给定子串字符匹配
                # 内层循环减小窗口数量
                if right - left < length:  # 比较当前长度与历史长度的大小，寻找最小长度
                    start = left
                    length = right - left
                # 先记录做窗口字符，在缩小窗口
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1  # 减小窗口数量
        return "" if length == float("inf") else s[start : start + length]

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        567. 字符串的排列
        """
        need, win = {}, {}
        for c in s1:
            need[c] = need.get(c, 0) + 1

        right, left = 0, 0
        vaild = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                win[c] = win.get(c, 0) + 1
                if win[c] == need[c]:
                    vaild += 1

            if vaild == len(need):
                return True

            if right - left == len(s1):  # 窗口缩小时机：窗口长度 == 给定的子串长度
                d = s2[left]
                left += 1
                if d in need:
                    if win[d] == need[d]:
                        vaild -= 1
                    win[d] -= 1
        return False

    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        438. 找到字符串中所有字母异位词
        """
        need, win = {}, {}
        for c in p:
            need[c] = need.get(c, 0) + 1

        left, right = 0, 0
        vaild = 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                win[c] = win.get(c, 0) + 1
                if win[c] == need[c]:
                    vaild += 1

            if vaild == len(need):
                res.append(left)

            if right - left == len(p):  # 窗口缩小时机：窗口长度 == 给定的子串长度
                d = s[left]
                left += 1
                if d in need:
                    if win[d] == need[d]:
                        vaild -= 1
                    win[d] -= 1
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        win = {}
        left, right = 0, 0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            win[c] = win.get(c, 0) + 1

            while win[c] > 1:  # 窗口缩小时机：新进来的字符重复
                d = s[left]
                left += 1
                win[d] -= 1

            res = max(res, right - left)
        return res

    def isPalindrome(self, s: str) -> bool:
        """
        125. 验证回文串
        """
        c = "".join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(c) - 1
        while left < right:
            if c[left] != c[right]:
                return False
            left += 1
            right -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        """
        5. 最长回文子串
        """

        def palidrome(s: str, l: int, r: int) -> int:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 两边扩散
                l -= 1
                r += 1
            return s[l + 1 : r]

        res = ""
        for i in range(len(s)):
            s1 = palidrome(s, i, i)  # 奇数情况
            s2 = palidrome(s, i, i + 1)  # 偶数情况
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        543. 二叉树的直径
        """
        self.res = 0
        traverse(root)

        def traverse(root: TreeNode) -> int:
            if not root:
                return 0
            leftDepth = traverse(root.left)
            rightDepth = traverse(root.right)
            self.res = max(self.res, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)

        return self.res

    def maxDepth(self, root: TreeNode) -> int:
        """
        104. 二叉树的最大深度
        """
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)

        # res = 0
        # depth = 0

        # def traverse(root):
        #     if not root:
        #         return res
        #     depth += 1   # 类似入栈+1
        #     if not root.left and not root.right:
        #         res = max(res, depth)
        #     traverse(root.left)
        #     traverse(root.right)
        #     depth -= 1  # 类似出栈-1

        # traverse(root)
        # return res

    def fib(self, n: int) -> int:
        """
        509. 斐波那契数
        """
        # if n < 2 :
        #     return n
        # return self.fib(n-1) + self.fib(n-2)

        # if n < 2:
        #     return n

        # dp = [0] * (n + 1)
        # dp[0] = 0
        # dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        self.memn = [-1] * (n + 1)

        def dp(memn, n):
            if n < 2:
                return n

            if self.memn[n] != -1:
                return self.memn[n]

            self.memn[n] = dp(self.memn, n - 1) + dp(self.memn, n - 2)
            return self.memn[n]

        return dp(self.memn, n)

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        322. 零钱兑换
        """

        def dp(coins, amount):
            if amount == 0:
                return 0

            if amount < 0:
                return -1

            if self.memo[amount] != -1000:
                return self.memo[amount]

            res = float("inf")

            for coin in coins:
                pathNum = dp(coins, amount - coin)
                if pathNum == -1:
                    continue
                pathNum += 1
                res = min(res, pathNum)
            self.memo[amount] = res if res != float("inf") else -1
            return self.memo[amount]

        self.memo = [-1000] * (amount + 1)
        return dp(coins, amount)

    def binary_search(self, nums: List[int], target: int):
        """
        二分查找
        """
        left, right = 0, len(nums) - 1  # 区间左闭右闭

        while left <= right:  # 保持左闭右闭
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = min - 1
        return -1

    def left_bound(self, nums: List[int], target: int):
        """
        二分查找（左侧边界）
        """
        left, right = 0, len(nums) - 1  # 区间左闭右闭

        while left <= right:  # 区间左闭右闭
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left < 0 or left >= len(nums):
            return -1
        return left if nums[left] == target else -1

    def right_bound(self, nums: List[int], target: int):
        """
        二分查找（右侧边界）
        """
        left, right = 0, len(nums) - 1  # 区间左闭右闭

        while left <= right:  # 区间左闭右闭
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right < 0 or right >= len(nums):
            return -1
        return right if nums[right] == target else -1


# 回文子串
# 最长回文子串
# 最长回文子序列
# 分割回文串

if __name__ == "__main__":
    s = Solution()
    s.coinChange([1, 2, 5], 11)
