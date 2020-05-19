"""day16_odd_even_linked_llist.py
    Created by Aaron at 19-May-20"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # app1
        # if head==None or head.next==None:
        #     return head
        # odd=head
        # even=head.next
        # l=[]
        # while odd:
        #     l.append(odd.val)
        #     try:
        #         odd=odd.next.next
        #     except AttributeError:
        #         break
        # while even:
        #     l.append(even.val)
        #     try:
        #         even=even.next.next
        #     except AttributeError:
        #         break
        # root=head2=ListNode(l[0])
        # for x in range(1,len(l)):
        #     root.next=ListNode(l[x])
        #     root=root.next
        # return head2

        # app2
        # if head==None or head.next==None:
        #     return head
        # head2=odd=head
        # even=head.next
        # l=[]
        # while even:
        #     try:
        #         if even.next!=None:
        #             odd.next=even.next
        #             odd=odd.next
        #         l.append(even.val)
        #         try:
        #             even=even.next.next
        #         except AttributeError:
        #             break
        #     except AttributeError:
        #         l.append(even.val)
        #         break
        # for x in l:
        #     odd.next=ListNode(x)
        #     odd=odd.next
        # return head2

        # app3
        if not head or not head.next: return head
        odd = head
        even = head.next
        evenhead = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenhead
        return head

run=Solution()
a=[1,2,3,4,5]
head=root=ListNode(a[0])
for x in range(1,len(a)):
    root.next=ListNode(a[x])
    root=root.next
res=run.oddEvenList(head)
while res:
    print(res.val)
    res=res.next
# app1 2 traversal 1 list to store
# app2 1 traversal 1 list to store while arranging odd
# app3 2 pointers