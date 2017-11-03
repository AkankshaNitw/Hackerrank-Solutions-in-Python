"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if head==None or head.next == None:
        return(head)
    
    if head.next.next == None:
        temp = head.next
        head.next.next = head
        head.next = None
        return(temp)
    
    nodei = head
    nodej = head.next
    nodek = head.next.next
    
    while nodek:
        nodej.next = nodei
        temp = nodej
        nodej = nodek
        nodek = nodek.next
        nodei = temp
        
    head.next = None
    nodej.next = nodei
    head = nodej
    
    return(head)