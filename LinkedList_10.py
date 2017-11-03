#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    node = head
    length = 0
    
    while(node):
        node = node.next
        length += 1
    
    strPosition = length - position
    
    node = head
    for _ in range(strPosition-1):
        node = node.next
        
    return node.data