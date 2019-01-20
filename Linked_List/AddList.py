# coding: utf-8
# 两个用链表代表的整数，其中每个节点包含一个数字。
# 数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。
# 写出一个函数将两个整数相加，用链表形式返回和。

# 如果是按原顺序存放，可以使用一个栈，计算当前sum和carry，放入另一个栈，再组成链表。


# Definition for singly-linked list.
class ListNode:
 def __init__(self, x):
     self.val = x
     self.next = None


class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        if l1 is None: return l2
        if l2 is None: return l1

        head1 = l1
        head2 = l2
        flag = 0  # carry

        while head1.next is not None or head2.next is not None:
            # 存在某一链表next为空时，构造next.val = 0，不影响加法结果
            if head1.next is None:
                head1.next = ListNode(0)
            if head2.next is None:
                head2.next = ListNode(0)

            sumNum = head1.val + head2.val
            if sumNum >= 10:
                head1.val = sumNum % 10  # 放在l1后面
                flag = 1
                head1.next.val += 1
            else:
                head1.val = sumNum
                flag = 0
            head1 = head1.next
            head2 = head2.next
        else:  # while...else...  这样也行诶，退出循环时加一步
            # 链表末尾时，单独处理，其和大于10时，追加节点
            head1.val = head1.val + head2.val
            if head1.val >= 10:
                head1.val = head1.val % 10
                head1.next = ListNode(1)
        return l1