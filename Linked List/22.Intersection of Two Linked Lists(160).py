class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(2)
node2 = ListNode(1)

node11 = ListNode(1)
node22 = ListNode(2)
node33 = ListNode(4)
node44 = ListNode(5)

node3 = ListNode(4)
node4 = ListNode(6)
node5 = ListNode(2)

node1.next = node2
node2.next = node3

node11.next = node22
node22.next = node33
node33.next = node44
node44.next = node3

node3.next = node4
node4.next = node5
node5.next = None

def collision_point(headA, headB, d):
    t1 = headA
    t2 = headB
    while (d):
        d -= 1
        t2 = t2.next
    while (t1 != t2):
        t1 = t1.next
        t2 = t2.next
    return t1

class Solution:
    def traversal(self, head):
        temp = head
        while(temp):
            print(temp.val)
            temp = temp.next

    def getIntersectionNode_brute1(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        temp1 = headA
        temp2 = headB
        while (temp1 != None):
            temp2 = headB
            while (temp2 != None):
                if (temp1 == temp2):
                    return temp1
                temp2 = temp2.next
            temp1 = temp1.next
        return None

    def getIntersectionNode_brute2(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        dict1 = {}
        temp1 = headA
        temp2 = headB
        while (temp1 != None):
            dict1[temp1] = 1
            temp1 = temp1.next
        while (temp2 != None):
            if (temp2 in dict1):
                return temp2
            temp2 = temp2.next
        return None

    def getIntersectionNode_better(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        temp1 = headA
        n1 = 0
        while (temp1 != None):
            n1 += 1
            temp1 = temp1.next
        temp2 = headB
        n2 = 0
        while (temp2 != None):
            n2 += 1
            temp2 = temp2.next
        if (n1 < n2):
            return collision_point(headA, headB, n2-n1)
        else:
            return collision_point(headB, headA, n1-n2)

    def getIntersectionNode_optimal(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        temp1 = headA
        temp2 = headB
        while(temp1 != temp2):
            temp1 = temp1.next
            temp2 = temp2.next
            if (temp1 == temp2):
                return temp1
            if (temp1 == None):
                temp1 = headB
            if (temp2 == None):
                temp2 = headA
        return temp1

node = Solution().getIntersectionNode_brute1(node1, node11)
print(node.val)
node = Solution().getIntersectionNode_brute2(node1, node11)
print(node.val)
node = Solution().getIntersectionNode_better(node1, node11)
print(node.val)
node = Solution().getIntersectionNode_optimal(node1, node11)
print(node.val)