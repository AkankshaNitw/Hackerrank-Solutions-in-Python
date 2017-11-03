"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    if headA == None:
        return headB
    
    if headB == None:
        return headA
    
    nodeA = headA
    nodeB = headB

    flagA = False
    flagB = False
    
    while nodeA and nodeB:
        while nodeA != None and nodeB!=None and nodeA.data<= nodeB.data :
            tempA = nodeA
            nodeA = nodeA.next
            flagA = True
            
        if flagA:
            tempA.next = nodeB
            flagA = False
            
        while nodeA != None and nodeB!=None and nodeB.data < nodeA.data:
            tempB = nodeB
            nodeB = nodeB.next
            flagB = True
            
        if flagB:
            tempB.next = nodeA
            flagB = False
            
    if headA.data <= headB.data:
        return headA
    else:
        return headB